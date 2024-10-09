from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action

from .serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    http_method_names = [name for name in viewsets.ModelViewSet.http_method_names if name != 'patch']
    serializer_class = BookSerializer
    queryset = BookSerializer.queryset()
    search_fields = ['title', 'authors__name'] # 'year', 'description', 'isbn', 'language', 'rating', 'publication_date', 'book_format', 'publisher'
    permission_classes = [IsAuthenticatedOrReadOnly]

class FavoriteViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    http_method_names = ['get', 'post', 'head', 'options']
    serializer_class = BookSerializer
    queryset = BookSerializer.queryset()
    permission_classes = [IsAuthenticated]

    @property
    def favorites(self):
        return self.request.user.favorites

    @action(detail=True, methods=['post'])
    def add(self, request, pk=None):
        if self.favorites.count() < 20:
           self.favorites.add(self.get_object())
        self.queryset = self.favorites.similar()
        return self.list(request)

    @action(detail=True, methods=['post'])
    def remove(self, request, pk=None):
        self.favorites.remove(self.get_object())
        self.queryset = self.favorites.similar()
        return self.list(request)


class AuthorViewSet(viewsets.ModelViewSet):
    http_method_names = [name for name in viewsets.ModelViewSet.http_method_names if name != 'patch']
    serializer_class = AuthorSerializer
    queryset = AuthorSerializer.queryset()
    search_fields = ['name']  # 'gender', 'description'
    permission_classes = [IsAuthenticatedOrReadOnly]


