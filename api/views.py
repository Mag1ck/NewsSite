import requests
from rest_framework import generics
from .forms import SearchForm
from django.db.models import Q
from .models import Article
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from .serializers import ArticleSerializer
from datetime import datetime

class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        ArticleTitle = self.request.query_params.get('ArticleTitle')
        content = self.request.query_params.get('content')
        images = self.request.query_params.get('image')
        return queryset

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'pk'

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        articletitle = self.kwargs.get('ArticleTitle')

        if pk is not None:
            return queryset.filter(pk=pk).first()
        elif articletitle is not None:
            return queryset.filter(ArticleTitle=articletitle).first()
        else:
            raise Http404("No matching queryset")



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
        results = Article.objects.filter(Q(ArticleTitle=search_query) | Q(content=search_query)) # Replace your_field with the field you want to search in

    return render(request, 'main/search.html', {'form': search, 'results': results})


def Kontent(request, ArticleTitle):
    url = f'https://danews.pl/api/{ArticleTitle}'

    # Send the request
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        post = response.json()
        formatted_date = datetime.strptime(post['date_added'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M')
        post['formatted_date'] = formatted_date
        # Return the post data
        return render(request, 'main/artykul.html', {'post': post})
    else:
        # Handle error
        raise Exception('Error fetching post from API')


def get_data(request, page):
    items_per_page = 10
    queryset = Article.objects.all()
    paginator = Paginator(queryset, items_per_page)
    data = list(paginator.page(page).object_list.values())
    return JsonResponse({'data': data}, safe=True)




