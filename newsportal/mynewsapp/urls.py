from django.contrib import admin
from django.urls import path
from mynewsapp import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('/<int:articleId>', views.showArticle),
    path('/author/<int:authorId>', views.ShowAuthor)
]
