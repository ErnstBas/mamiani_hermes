from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "article/index.html")

def articles(request):
    pass

def article_detail(request):
    pass


