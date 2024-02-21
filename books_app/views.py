from django.shortcuts import render
from rest_framework import generics
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
    
    
    


    