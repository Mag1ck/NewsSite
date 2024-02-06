from django.urls import path,include
from . import views





urlpatterns = [

    path("",views.fetch_posts,name="homepage"),
    path("edit/", views.edit,name="editor"),
    path("", include('api.urls')),

]

