from .models import Account
from rest_framework.generics import CreateAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import AllowAny
from settings.mixins  import QuerySetMixin

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
