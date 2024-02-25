from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'price', 'price', 'publish', 'slug', 'description')
        
    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        price = data.get('price', None)
        if not title.isalpha():
            raise ValidationError({'status' : False, 'message' : 'book title must be literals!'})
        
        if not author.isalpha():
            raise ValidationError({'status' : False, 'message' : 'book author must be literals!'})
        
        if Book.objects.filter(author=author, title=title).exists():
            raise ValidationError({'status' : False, 'message' : 'this book already exist!'})
        
        return data
    
    


class BooksSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    slug = serializers.SlugField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    create = serializers.DateTimeField()
    publish = serializers.DateTimeField()
