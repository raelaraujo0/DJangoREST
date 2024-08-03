from django.urls import path
from App.views import books_view, change_and_delete_Books

urlpatterns = [
    path('', books_view),
    path('/<int:pk>/', change_and_delete_Books),
]