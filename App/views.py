from App.models import Books
from App.serializers import BooksSerial

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view

@api_view(['GET'])
def getBook(request):
    books = Books.objects.all()
    serializer = BooksSerial(books, many = True)
    return Response({'msg':'All the book is here rn!'}, status = status.HTTP_200_OK)

@api_view(['POST'])
def postBook(request):
    serializer = BooksSerial(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Books created successfully'}, status = status.HTTP_201_CREATED)
    return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def putBook(request):
    books = Books.objects.get(pk = request.data.get('id'))
    serializer = BooksSerial(books, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Book updated successfully'}, status = status.HTTP_200_OK)
    return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteBook(request):
    books = Books.objects.get(pk = request.data.get('id'))
    books.delete()
    return Response({'msg':'The book has been deleted'}, status = status.HTTP_204_NO_CONTENT)