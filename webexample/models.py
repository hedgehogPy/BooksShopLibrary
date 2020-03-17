from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from django import forms


def gen_slug(s):
    new_slug = slugify(s,allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Genre(models.Model):
    name = models.CharField(max_length=50, db_index = True)
    slug = models.SlugField(max_length=50,unique = True,blank = True)
    info = models.TextField(max_length=100)
    photo = models.CharField(max_length = 500)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('genre_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('genre_update_url',kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('genre_delete_url',kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args,**kwargs)



class Author(models.Model):
    first_name = models.CharField(max_length=50, db_index = True)
    second_name = models.CharField(max_length=50, db_index = True)
    info = models.TextField(max_length=100)
    slug = models.SlugField(max_length=50,unique = True,blank = True)
    photo = models.CharField(max_length = 500)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('author_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('author_update_url',kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('author_delete_url',kwargs={'slug': self.slug})

    def __str__(self):
        return self.second_name+self.first_name

    def save(self,*args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.first_name)
        super().save(*args,**kwargs)

class Book(models.Model):
    name = models.CharField(max_length=50, db_index = True)
    info = models.TextField(max_length=100,db_index = True)
    slug = models.SlugField(unique = True, blank = True)
    price = models.IntegerField()
    recomAge = models.IntegerField()
    author = models.ManyToManyField(Author,related_name="books")
    genres = models.ManyToManyField(Genre,related_name="books")
    photo = models.CharField(max_length = 500)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('book_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('book_update_url',kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('book_delete_url',kwargs={'slug': self.slug})

    def get_info_url(self):
        return reverse('book_info_url',kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args,**kwargs)


class Client(models.Model):
    fullname = models.CharField(max_length=50, db_index = True)
    nickname = models.CharField(max_length=50, db_index = True)

    def __str__(self):
        return '{}'.format(self.fullname)

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(db_index = True)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return '{}'.format(self.address)

class BookOrder(models.Model):
    quantity = models.IntegerField()
    books = models.ManyToManyField(Book)
    orders = models.ManyToManyField(Order)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return '{}'.format(self.quantity)
