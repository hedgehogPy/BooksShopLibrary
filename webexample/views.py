from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse,reverse_lazy
from .models import Book,Author,Genre,Order,BookOrder,User
from .forms import AuthorForm,GenreForm,BookForm
from .utils import *
from .urls import *
from django.db.models import Q


# Create your views here.

def home_page(request):
    return render(request, 'webexample/homepage.html')

def books_list(request):
    search_query = request.GET.get('search','')
    if(search_query):
        books = Book.objects.filter(Q(name__icontains=search_query)).order_by('-date')
    else:
        books = Book.objects.all().order_by('-date')
    return render(request, 'webexample/index.html', context = {'books':books})

def authors_list(request):
    search_query = request.GET.get('search','')
    if(search_query):
        authors = Author.objects.filter(Q(first_name__icontains=search_query) | Q(second_name__icontains=search_query) | Q(info__icontains=search_query).order_by('-date'))
    else:
        authors = Author.objects.all().order_by('-date')
    return render(request, 'webexample/index2.html', context = {'authors':authors})

def genres_list(request):
    search_query = request.GET.get('search','')
    if(search_query):
        genres = Genre.objects.filter(Q(name__icontains=search_query)| Q(info__icontains=search_query).order_by('-date'))
    else:
        genres = Genre.objects.all().order_by('-date')
    return render(request, 'webexample/index3.html', context = {'genres':genres})

def stats_genre(request):
    quantity = Book.objects.all().count()
    genres = Genre.objects.all()
    d = dict()
    for genre in genres:
        d[genre.name] = genre.books.count()*100/quantity
    return render(request, 'webexample/stats_genre.html', context = {'d':d})

def stats_author(request):
    quantity = Book.objects.all().count()
    authors = Author.objects.all()
    d = dict()
    for author in authors:
        fullname = author.first_name + " " + author.second_name
        d[fullname] = author.books.count()*100/quantity
    return render(request, 'webexample/stats_genre.html', context = {'d':d})

def book_list_by_genre(request,slug):
    genre = Genre.objects.get(slug__iexact=slug)
    return render(request, 'webexample/index31.html',context = {'genre':genre})

def book_list_by_author(request,slug):
    author = Author.objects.get(slug__iexact=slug)
    return render(request, 'webexample/index32.html',context = {'author':author})

def book_info(request,slug):
    book = Book.objects.get(slug__iexact=slug)
    return render(request,'webexample/index33.html', context={'book':book})

class BookDetail(ObjectDetailMixin,View):
    model = Book
    template = 'webexample/book_detail.html'

class AuthorDetail(ObjectDetailMixin,View):
    model = Author
    template = 'webexample/author_detail.html'

class GenreDetail(ObjectDetailMixin,View):
    model = Genre
    template = 'webexample/genre_detail.html'

class AuthorCreate(ObjectCreateMixin,View):
    model_form = AuthorForm
    template = "webexample/author_create.html"
    raise_exception = True

class GenreCreate(ObjectCreateMixin,View):
    model_form = GenreForm
    template = "webexample/genre_create.html"
    raise_exception = True

class BookCreate(ObjectCreateMixin,View):
    model_form = BookForm
    template = "webexample/book_create.html"
    raise_exception = True

class GenreUpdate(ObjectUpdateMixin,View):
    model = Genre
    model_form = GenreForm
    template = 'webexample/genre_update_form.html'
    raise_exception = True

class AuthorUpdate(ObjectUpdateMixin,View):
    model = Author
    model_form = AuthorForm
    template = 'webexample/author_update_form.html'
    raise_exception = True

class BookUpdate(ObjectUpdateMixin,View):
    model = Book
    model_form = BookForm
    template = 'webexample/book_update_form.html'
    raise_exception = True

class GenreDelete(View):
    def get(self,request,slug):
        genre = Genre.objects.get(slug__iexact=slug)
        return render(request,'webexample/genre_delete_form.html',context={'genre':genre})

    def post(self,request,slug):
        genre = Genre.objects.get(slug__iexact=slug)
        genre.delete()
        genres = Genre.objects.all()
        return render(request, 'webexample/index3.html', context = {'genres':genres})

class AuthorDelete(View):
    def get(self,request,slug):
        author = Author.objects.get(slug__iexact=slug)
        return render(request,'webexample/author_delete_form.html',context={'author':author})

    def post(self,request,slug):
        author = Author.objects.get(slug__iexact=slug)
        author.delete()
        authors = Author.objects.all()
        return render(request, 'webexample/index2.html', context = {'authors':authors})

class BookDelete(View):
    def get(self,request,slug):
        book = Book.objects.get(slug__iexact=slug)
        return render(request,'webexample/book_delete_form.html',context={'book':book})

    def post(self,request,slug):
        book = Book.objects.get(slug__iexact=slug)
        book.delete()
        books = Book.objects.all()
        return render(request, 'webexample/index.html', context = {'books':books})
