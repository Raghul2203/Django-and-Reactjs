from django.contrib.auth.models import User
from rest_framework import serializers
# from .models import Profile 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
