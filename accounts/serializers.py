from typing import ClassVar

from rest_framework import serializers

from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = CustomUser
        fields: ClassVar= [
            'username',
            'email',
            'password',
            'role',
        ]

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            role=validated_data.get('role', CustomUser.Role.MEMBER),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user