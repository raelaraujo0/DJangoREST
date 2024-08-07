from django.urls import path
from App.views import CreateAndListBooks, ChangeAndDeleteBooks

urlpatterns = [
    path('', CreateAndListBooks.as_view()),
    path('/<int:pk>/', ChangeAndDeleteBooks.as_view()),
]