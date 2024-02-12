from django.urls import path,include
from . import views
from django.views.generic import TemplateView




urlpatterns = [

    path("",views.fetch_posts,name="homepage"),
    path("edit/", views.edit,name="editor"),
    path("", include('api.urls')),
    path("robots.txt",TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain")),           
]

