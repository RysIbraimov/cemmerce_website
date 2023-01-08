from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        new_user = User(username=validated_data['username'])
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user



