from django.urls import path

from .views import ArticleList, ArticleDetail, add_article, search_view, Kontent

urlpatterns = [
    path('api/', ArticleList.as_view()),
    path('edit/', add_article),
    path('api/<int:pk>/', ArticleDetail.as_view()),
    path('search/', search_view, name='search_view'),
    path('api/<str:slug>/', ArticleDetail.as_view()),
    path('artykul/<str:slug>/', Kontent, name='article-detail'),
]
