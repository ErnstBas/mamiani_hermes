    
from django.urls import path

from . import views

urlpatterns =[
    path("authors", views.articles, name="authors-page"),
    path("authos/<slug:slug>", views.article_detail, name="author-detail-page")
]