# books/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import status

from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer,OrderedBookSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__name']

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




##order 
 

class BookOrderView(APIView):
    def post(self, request):
        print("DATA RECEIVED:", request.data)  # Debug line
        data = request.data
        student_id = data.get("student_id")
        books = data.get("books", [])

        if not student_id or not books:
            return Response({"error": "student_id and books are required"}, status=status.HTTP_400_BAD_REQUEST)

        saved = []
        for book in books:
            book["student_id"] = student_id  # প্রতিটি বইয়ের সাথে student_id যুক্ত করছি
            serializer = OrderedBookSerializer(data=book)
            if serializer.is_valid():
                serializer.save()
                saved.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"success": True, "data": saved}, status=status.HTTP_201_CREATED)