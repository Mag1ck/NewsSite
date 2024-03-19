from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import login_view
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import MySitemap

sitemaps={

    'posts' :MySitemap
}

urlpatterns = [

    path("",views.fetch_posts,name="homepage"),
    path("edit/", views.edit,name="editor"),
    path("", include('api.urls')),
    path("robots.txt",TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain")),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},name='django.contrib.sites.views.sitemap')
]

