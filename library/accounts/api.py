from .models import Account
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets, mixins

from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from settings.mixins  import QuerySetMixin

from books.serializers  import BookSerializer
from books.api import BookViewSet


class RegisterAccountSerializer(QuerySetMixin, ModelSerializer):

    class Meta:
        model = Account
        fields = 'email', 'password'
        extra_kwargs = {'password': {'write_only': True, 'required':True}, 'email': {'required':True}}

    def create(self , data):
        obj = self.Meta.model(**data)
        obj.set_password(obj.password)
        return super().create({'email': obj.email, 'username': obj.email, 'password':obj.password})

class RegisterApiView(CreateAPIView):
    authentication_classes = []  # it should be AllowAny
    serializer_class = RegisterAccountSerializer
    queryset = RegisterAccountSerializer.queryset()


class BookViewSet(viewsets.ModelViewSet):
    @action(detail=True, methods=['post'])
    def add(self, request, pk=None):
        book = self.get_object()
        queryset = request.user.favorites
        if queryset.count() < 20:
            queryset.add(book)
        self.queryset = queryset.similar()
        return self.list(request=request)

    @action(detail=True, methods=['post'])
    def remove(self, request, pk=None):
        book = self.get_object()
        queryset = request.user.favorites
        queryset.remove(book)
        return self.list(request=request)