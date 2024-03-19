from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import path

from main.views import login_view

from .views import ArticleList,ArticleDetail,add_article,search_view,Kontent,get_tags


urlpatterns = [
    path('api/', ArticleList.as_view()),
    path('edit/',add_article ),
    path('api/<int:pk>/', ArticleDetail.as_view()),
    path('search/', search_view, name='search_view'),
    path('api/<str:slug>/',ArticleDetail.as_view()),
    path('artykul/<str:slug>/', Kontent, name='article-detail'),
    path('tags/', get_tags, name='get_tags'),
]