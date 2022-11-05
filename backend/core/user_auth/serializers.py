from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh_token = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh_token'] = str(refresh_token)
        data['access_token'] = str(refresh_token.access_token)

        return data
