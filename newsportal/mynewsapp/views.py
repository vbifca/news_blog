from django.shortcuts import render
from .models import Article, Author
# Create your views here.
# импорт Api новостей
from django.shortcuts import render
from newsapi import NewsApiClient

# Создание функции представления
def index(request):

    # newsapi = NewsApiClient(api_key ='8cbff10e995840129517f28212262aec')
    # top = newsapi.get_top_headlines(sources ='techcrunch')
    #
    # l = top['articles']
    # dsc =[]
    # nws =[]
    # im =[]
    #
    # for i in range(len(l)):
    #   f = l[i]
    #   nws.append(f['title'])
    #   dsc.append(f['description'])
    #   im.append(f['urlToImage'])
    #   mylist = zip(nws, dsc, im)

    news = Article.objects.all()
    n = {"news":news}
    return render(request, 'index.html', n)

def showArticle(request, articleId):
    article = Article.objects.get(id=articleId)
    n = {"article": article, "author": Author.objects.get(id=article.author.id)}
    return render(request, 'ShowArticle.html', n)

def ShowAuthor(request, authorId):
    author = Author.objects.get(id=authorId)
    n = {"author": author, "article": Article.objects.filter(author = authorId)}
    return render(request, 'author.html', n)