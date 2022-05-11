from unicodedata import category
from django.shortcuts import render
from .models import Articles,Category

# Create your views here.

def home(request):

    list_article=Articles.objects.all()

    context={"liste_articles":list_article}

    return render(request,"index.html",context)


def detail(request,id_article):

    article=Articles.objects.get(id=id_article)
    category= article.category
    article_en_relation=Articles.objects.filter(category=category)[:7]
    return render(request,"detail.html",{"article":article,'aer':article_en_relation})
