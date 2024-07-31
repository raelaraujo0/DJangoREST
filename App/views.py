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
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)