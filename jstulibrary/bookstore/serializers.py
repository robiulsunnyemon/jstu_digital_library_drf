# books/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Category,OrderedBook,PopularBook

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



##Popular Book
    

class PopularBookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )

    class Meta:
        model = PopularBook
        fields = '__all__'

    def create(self, validated_data):
        return PopularBook.objects.create(**validated_data)

    def create_bulk(self, validated_data_list):
        return PopularBook.objects.bulk_create([PopularBook(**item) for item in validated_data_list])




## order
 
class OrderedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedBook
        fields = '__all__'




##user account

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user
