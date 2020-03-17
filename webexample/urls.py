from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home_page_url'),
    path('book/', views.books_list, name = 'books_list_url'),
    path('book/stats_genre/',views.stats_genre, name = 'genre_stats_url'),
    path('book/stats_author/',views.stats_author, name = 'author_stats_url'),
    path('book/create/', views.BookCreate.as_view(), name = 'book_create_url'),
    path('book/<str:slug>/', views.BookDetail.as_view(), name = 'book_detail_url'),
    path('book/<str:slug>/info/', views.book_info, name = 'book_info_url'),
    path('book/<str:slug>/update/', views.BookUpdate.as_view(), name ='book_update_url'),
    path('book/<str:slug>/delete/', views.BookDelete.as_view(), name ='book_delete_url'),

    path('author/',views.authors_list, name = 'authors_list_url'),
    path('author/create/', views.AuthorCreate.as_view(), name ='author_create_url'),
    path('author/<str:slug>/', views.AuthorDetail.as_view(), name ='author_detail_url'),
    path('author/<str:slug>/update/', views.AuthorUpdate.as_view(), name ='author_update_url'),
    path('author/<str:slug>/delete/', views.AuthorDelete.as_view(), name ='author_delete_url'),

    path('author/<str:slug>/books/', views.book_list_by_author, name ='book_list_by_author'),

    path('genre/', views.genres_list, name = 'genres_list_url'),
    path('genre/create/', views.GenreCreate.as_view(), name ='genre_create_url'),
    path('genre/<str:slug>/', views.GenreDetail.as_view(), name ='genre_detail_url'),
    path('genre/<str:slug>/update/', views.GenreUpdate.as_view(), name ='genre_update_url'),
    path('genre/<str:slug>/delete/', views.GenreDelete.as_view(), name ='genre_delete_url'),

    path('genre/<str:slug>/books/', views.book_list_by_genre, name ='book_list_by_genre')
 ]
