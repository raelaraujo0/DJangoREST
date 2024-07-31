from django.urls import path
from App.views import books_view

urlpatterns = [
    path('', books_view),
]