import requests
from rest_framework import generics
from .forms import SearchForm
from django.db.models import Q
from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from .serializers import ArticleSerializer
from datetime import datetime
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage


class CustomPagination(PageNumberPagination):
    page_size = 3  # Default page size for pages after the first
    page_size_query_param = 'page_size'
    max_page_size = 5  # Maximum page size allowed

    def get_page_size(self, request):
        # Check if the request is for the first page
        if request.query_params.get(self.page_query_param) == "1":
            # For the first page, return 2 items per page
            return 2
        elif self.page_size_query_param in request.query_params:
            try:
                # Get the requested page size from the query parameters
                page_size = int(request.query_params[self.page_size_query_param])
                # Ensure the page size does not exceed the maximum allowed
                return min(page_size, self.max_page_size)
            except (ValueError, TypeError):
                # In case of any error, or if the provided page size is less than 1,
                # ignore the provided page size and fall back to the default page size.
                pass

        # For any other case, use the default page size
        return super().get_page_size(request)


class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('-date_added')
    pagination_class = CustomPagination  # Specify the custom pagination class

    def get_queryset(self):
        queryset = super().get_queryset()
        article_title = self.request.query_params.get('article_title')
        content = self.request.query_params.get('content')
        images = self.request.query_params.get('image')
        if article_title:
            queryset = queryset.filter(article_title__icontains=article_title)
        if content:
            queryset = queryset.filter(content__icontains=content)
        if images:
            queryset = queryset.filter(images__icontains=images)
        return queryset

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save()
        else:
            raise PermissionDenied("Only authenticated users can add articles")

    @method_decorator(login_required)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Sprawdzenie, czy użytkownik jest właścicielem artykułu
        if instance.author != request.user:
            raise PermissionDenied("You do not have permission to delete this article")

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


def group_required(group_name):
    """
    Decorator for views that checks whether a user is in a particular group,
    redirecting to the log-in page if necessary.
    """

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied("You do not have permission to access this page")

        return _wrapped_view

    return decorator


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('-date_added')
    lookup_field = 'pk'

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')

        if pk is not None:
            return queryset.filter(pk=pk).first()
        elif slug is not None:
            return queryset.filter(slug=slug).first()
        else:
            raise Http404("No matching queryset")

    @method_decorator(group_required('Redaktor'))
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Sprawdzenie, czy użytkownik należy do grupy redaktorów
        # Za pomocą dekoratora group_required
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


def add_article(request):
    if request.method == "POST":
        form = Article(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            article = form.save(commit=False)  # Create an article object without saving to database yet
            article.save()  # Save the article to the database
            return redirect('edit')  # Redirect to the 'edit' URL or whatever appropriate URL name you have
    else:
        form = Article()


def search_view(request):
    search = SearchForm(request.GET)
    results = None

    if search.is_valid():
        search_query = search.cleaned_data.get('search_query')
        results = Article.objects.filter(Q(ArticleTitle=search_query) | Q(
            content=search_query))  # Replace your_field with the field you want to search in

    return render(request, 'main/search.html', {'form': search, 'results': results})


def Kontent(request, slug):
    url = f'http://127.0.0.1:8000/api/{slug}'

    # Send the request
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        post = response.json()
        formatted_date = datetime.strptime(post['date_added'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M')
        post['formatted_date'] = formatted_date

        canonical_url = request.build_absolute_uri()

        # Return the post data
        return render(request, 'main/artykul.html', {'post': post, 'canonical_url': canonical_url})
    else:
        # Handle error
        raise Exception('Error fetching post from API')
