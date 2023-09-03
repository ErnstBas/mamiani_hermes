from django.urls import path

from . import views

urlpatterns =[
    path("", views.starting_page, name="starting-page"),
    path("articles", views.articles, name="articles-page"),
    path("articles/<slug:slug>", views.article_detail, name="article-detail-page")
]

