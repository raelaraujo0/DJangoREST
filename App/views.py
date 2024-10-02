from App.models import Books
from App.serializers import BooksSerial

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view

<<<<<<< HEAD
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
        return Response(serializer.erros, status = HTTP_400_BAD_REQUEST)
=======
def BookListAndCreate(APIView):
    def getObj(self, pk):
        try:
            return Books.objects.all(pk =pk)
        except Books.DoesNotExist:
            raise Response({'msg': 'ive dont found the book :('}, status = status.HTTP_404_NOT_FOUND)
    
    def get(self, request):
        book = self.Books.objects.all()
        serializer = BooksSerial(book, many = True)
        return Response({'msg':'All the book is here rn! :D'}, serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        book = self.getObj(pk)
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
            return Response({'msg':'Book updated successfully'}, serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        book = self.getObj(pk)
        Books.delete()
        return Response({'msg':'The book has been deleted'}, status = status.HTTP_204_NO_CONTENT)        

>>>>>>> master
