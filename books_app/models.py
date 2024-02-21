from django.db import models
from autoslug import AutoSlugField


class Book(models.Model): # BOOK model
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    create = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=True)
    
    # slug = AutoSlugField(populate_from='title', always_update=True)
    
    
    