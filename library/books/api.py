from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    http_method_names = [name for name in viewsets.ModelViewSet.http_method_names if name != 'patch']
    serializer_class = BookSerializer
    queryset = BookSerializer.queryset()
    filterset_fields = ['title', 'authors__name'] # 'year', 'description', 'isbn', 'language', 'rating', 'publication_date', 'book_format', 'publisher'
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorViewSet(viewsets.ModelViewSet):
    http_method_names = [name for name in viewsets.ModelViewSet.http_method_names if name != 'patch']
    serializer_class = AuthorSerializer
    queryset = AuthorSerializer.queryset()
    filterset_fields = ['name']  # 'gender', 'description'
    permission_classes = [IsAuthenticatedOrReadOnly]
