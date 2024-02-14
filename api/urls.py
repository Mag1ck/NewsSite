from django.urls import path
from .views import ArticleList,ArticleDetail,add_article,search_view,Kontent,get_data


urlpatterns = [
    path('api/', ArticleList.as_view()),
    path('edit/',add_article ),
    path('api/<int:pk>/',ArticleDetail.as_view()),
    path('search/', search_view, name='search_view'),
    path('get_data/<int:page>/', get_data, name='get_data'),
    path('api/<str:slug>/', ArticleDetail.as_view()),
    path('<str:slug>/', Kontent),
]