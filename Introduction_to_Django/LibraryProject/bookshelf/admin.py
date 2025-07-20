from django.contrib import admin
from .models import Book

admin.site.register(Book)

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','auther','publication_year')
    list_filter = ('publication_year','auther')
    search_fields = ('title','auther')


