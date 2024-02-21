from django.shortcuts import render, redirect
from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


class BookListApiView(generics.ListAPIView): # List
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveAPIView(generics.RetrieveAPIView): # Detail
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView): # Detail & Delete
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView): # Detail & Update
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): # Detail & Update & Delete
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListAPIView(APIView): # List
    def get(self, request):
        books = Book.objects.all()
        serialized_books = BookSerializer(books, many=True)
        data = {
            'status' : 'ok',
            "APIView books:" : serialized_books.data
        }
        return Response(data)
        
class BookCreateAPIView(APIView): # List

    def post(self, request):
        book = request.data
        print(book)
        serializer_book = BookSerializer(data=book)
        # print(serializer_book)
        if serializer_book.is_valid():
            serializer_book.save()
            return Response({'status' : 'book created', 'created book' : serializer_book})
        else:
            return Response({'status' : 'book did not created!'})

class BookDetailAPIView(APIView): # List
    def get(self, request, pk):
        books = Book.objects.get(id=pk)
        serialized_books = BookSerializer(books)
        data = {
            'status' : 'ok',
            "APIView detail:" : serialized_books.data
        }
        return Response(data)



    