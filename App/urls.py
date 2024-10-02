from rest_framework.routers import DefaultRouter
from App.views import getBook, postBook, deleteBook
from django.urls import path, include

urlpatterns = [
    path('', getBook),
    path('<int:pk>/', deleteBook)
]