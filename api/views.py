from rest_framework import generics
from .forms import SearchForm
from django.db.models import Q
from .models import Article
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .serializers import ArticleSerializer

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


def test(request):
    return render(request,'main/test.html')


def get_data(request, page):
    items_per_page = 10
    queryset = Article.objects.all()
    paginator = Paginator(queryset, items_per_page)
    data = list(paginator.page(page).object_list.values())
    return JsonResponse({'data': data}, safe=False)




