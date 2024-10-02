from rest_framework.routers import DefaultRouter
from App.views import BookListAndCreate
from django.urls import path, include

urlpatterns = [
    path('', BookListAndCreate.as_view()),
    path('<int:pk>/', BookListAndCreate.as_view())
]