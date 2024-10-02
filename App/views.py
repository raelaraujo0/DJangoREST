from App.models import Books
from App.serializers import BooksSerial

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view

class BookListAndCreate(APIView):
    def getObj(self, pk):
        try:
            return Books.objects.get(pk = pk)
        except Books.DoesNotExist:
            raise NotFound()
    
    def get(self, request):
        book = Books.objects.all()
        serializer = BooksSerial(book, many = True)
        return Response({'msg':'All the book is here rn! :D'}, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BooksSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Books created successfully'}, status = status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        book = self.getObj(pk)
        serializer = BooksSerial(books, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Book updated successfully'}, status = status.HTTP_200_OK)
        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        book = self.getObj(pk)
        Books.delete()
        return Response({'msg':'The book has been deleted'}, status = status.HTTP_204_NO_CONTENT)        

