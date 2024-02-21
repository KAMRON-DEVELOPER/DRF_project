from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author')
    list_display = ('title', 'author', 'price', 'create', 'publish', 'slug')
    # prepopulated_fields = {"slug": ("title",)} tuple
    ordering = ('publish',)

admin.site.register(Book, BookAdmin)


