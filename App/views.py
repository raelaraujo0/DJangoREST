from App.models import Books
from App.serializers import BooksSerial

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

class CreateAndListBooks(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BooksSerial(books, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BooksSerial(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ChangeAndDeleteBooks(APIView):
    def findObject(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        books = self.findObject(pk)
        serializer = BooksSerial(books)
        return Response(serializer.data)

    def put(self, request, pk):
        books = self.findObject(pk)
        serializer = BooksSerial(books, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) ## o PUT ja da o respose, nao precisa de status
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        books = self.findObject(pk)
        books.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)