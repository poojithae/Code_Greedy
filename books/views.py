from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter
from django.shortcuts import render,redirect
from books.forms import Bookform



# API view for listing and creating books
# API view for listing and creating books
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BookSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
      
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view for retrieving, updating, or deleting a book
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Custom pagination class
class CustomPagination(PageNumberPagination):
    page_size = 10  # Default number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Maximum number of items per page

# API view for filtering books
@api_view(['GET'])
def filtered_book_list(request):
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    
    # Apply filtering
    queryset = filterset_class(request.query_params, queryset=queryset).qs
    
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)

# API view for marking a book as favorite
@api_view(['POST'])
def mark_favorite(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    book.is_favorite = True
    book.save()
    return Response({'message': 'Book marked as favorite'})


def books(request):
    Books=Book.objects.all()
    return render(request,'books/allbookdetails.html',{'Books':Books})

# def booksall(request):
#      Books=Book.objects.all()
#      return render(request,'books/allbooksdetail.html',{'Books':Books})

def create(request):
    form=Bookform()
    if request.method=='POST':
        form=Bookform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/books')
    return render(request,'books/create.html',{'form':form})
 

def delete(request,pk):
    Books=Book.objects.get(pk=pk)
    Books.delete()
    return redirect('/books')

def singledetails(request,pk):
     d=Book.objects.get(pk=pk)
     return render(request,'books/singlebook.html',{'d':d})

def update(request,pk):
     e=Book.objects.get(pk=pk)
     if request.method=='POST':
      form=Bookform(request.POST,instance=e)
      if form.is_valid():
          form.save()
      return redirect('/books')
     return render(request,'books/update.html',{'e':e})

def aboutus(request):
    return render(request,'books/aboutus.html')
def services(request):
    return render(request,'books/services.html')
def Home(request):
    return render(request,'books/Home.html')