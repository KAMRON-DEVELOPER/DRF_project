from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group


class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'location')
    list_display = ('username', 'location', 'birth_date')
    ordering = ('birth_date',)

admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)


