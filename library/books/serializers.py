from .models  import Book, Author
from rest_framework import serializers
from settings.mixins  import QuerySetMixin


class BookSerializer(QuerySetMixin, serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(QuerySetMixin, serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
