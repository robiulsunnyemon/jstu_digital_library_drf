# books/admin.py

from django.contrib import admin
from .models import Book, Category,OrderedBook

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'writer', 'fee', 'available']
    list_filter = ['available', 'category']
    search_fields = ['name', 'writer']



@admin.register(OrderedBook)
class OrderedBookAdmin(admin.ModelAdmin):
    list_display=['id','name','fee','student_id','fee','counter','counter','counter_price']
   



