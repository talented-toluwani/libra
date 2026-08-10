from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    bio = serializers.CharField()
    created_at = serializers.DateTimeField()