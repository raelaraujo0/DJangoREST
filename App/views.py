from App.models import Books
from App.serializers import BooksSerial
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def books_view(request):
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerial(books, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BooksSerial(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def change_and_delete_Books(request, pk):
    try:
        books = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BooksSerial(books)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BooksSerial(books, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) ## o PUT ja da o respose, nao precisa de status
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        books.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)