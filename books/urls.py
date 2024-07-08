# books/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('api/books/', views.book_list, name='book-list'),
    # path('api/books/<int:pk>/', views.book_detail, name='book-detail'),
    path('books/', views.books),
    path('created/', views.create,name='book-create'),
    path('delete/<int:pk>/', views.delete ,name='book-delete'),
    path('singledetails/<int:pk>/', views.singledetails ,name='book-singledetails'),
    path('update/<int:pk>/', views.update ,name='book-update'),
    path('aboutus/', views.aboutus ,name='book-aboutus'),
    path('services/', views.services ,name='book-services'),
    path('Home/', views.Home ,name='book-Home'),
]   
