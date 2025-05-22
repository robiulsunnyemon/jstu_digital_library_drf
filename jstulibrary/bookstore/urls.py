# books/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CategoryViewSet,BookOrderView,PopularBookViewSet,RegisterView,LoginView

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'popular_books', PopularBookViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/', BookOrderView.as_view(), name='book-order'),
    path('register/', RegisterView.as_view(), name='register'),
     path('login/', LoginView.as_view(), name='api-login'),
     path('apii/medicine_n/<str:name>/', medicine_by_name, name='medicine_by_name'),
   
]
