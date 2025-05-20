# books/serializers.py

from rest_framework import serializers
from .models import Book, Category,OrderedBook

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def create_bulk(self, validated_data_list):
        return Book.objects.bulk_create([Book(**item) for item in validated_data_list])



## order
 
class OrderedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedBook
        fields = '__all__'