from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField('Имя', max_length = 50)
    lastname = models.CharField('Фамилия', max_length = 50)
    about = models.TextField('О себе')
    photo = models.ImageField(upload_to = 'images')
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('Название', max_length = 50)
    discription = models.CharField('Описание', max_length = 250)
    content = models.TextField('Статья')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    href = models.TextField('Ссылка на оригинал')
    photo = models.ImageField(upload_to = 'images')

    def __str__(self):
        return self.title

