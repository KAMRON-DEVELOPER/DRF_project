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


# **************** APIView ****************
class BookListAPIView(APIView): # List
    def get(self, request):
        books = Book.objects.all()
        serialized_books = BookSerializer(books, many=True)
        data = {'status' : 'ok', "APIView books:" : serialized_books.data}
        return Response(data)
        
class BookCreateAPIView(APIView): # List

    def post(self, request):
        book = request.data # book is json or object(dictionary)
        print(book)
        serializer_book = BookSerializer(data=book)
        # print(serializer_book)
        if serializer_book.is_valid():
            serializer_book.save()
            return Response({'status' : 'book created', 'created book' : serializer_book.data})
        else:
            return Response({'status' : 'book did not created!'})

class BookDetailAPIView(APIView): # List
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serialized_books = BookSerializer(book)
        data = {'status' : 'ok', "APIView detail:" : serialized_books.data}
        return Response(data)

class BookDeleteAPIView(APIView): # List
    def delete(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        data = {'status' : 'ok', "APIView message:" : "the book has been deleted"}
        return Response(data)

class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        updated_book = request.data
        serialized_updated_book = BookSerializer(instance=book, data=updated_book, partial=True)
        if serialized_updated_book.is_valid():
            serialized_updated_book.save()
            data = {'status' : 'ok', 'APIView update' : serialized_updated_book.data}
            return Response(data)
        else:
            return Response({'status' : 'failure', 'message' : 'did not updated'})
    
    


    