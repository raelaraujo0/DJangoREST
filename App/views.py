from App.models import Books
from App.serializers import BooksSerial

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

class CreateAndListBooks(generics.ListCreateAPIView):
    queryset = books.objects.all()
    serializer_class = BooksSerial

class ChangeAndDeleteBooks(generics.RetrieveUpdateDestroyAPIView):
    queryset = books.objects.all()
    serializer_class = BooksSerial