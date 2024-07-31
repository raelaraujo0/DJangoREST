from App.models import Books
from rest_framework import serializers

class BooksSerial(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'name', 'author', 'readed', 'created_at']