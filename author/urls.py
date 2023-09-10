    
from django.urls import path

from . import views

urlpatterns =[
    path("authors", views.articles, name="authors-page"),
    path("authos/<slug:slug>", views.author_detail, name="author-detail-page")
]