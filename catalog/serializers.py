from typing import ClassVar

from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
    queryset=Author.objects.all(),
    source="author",
    write_only=True
)
    class Meta:
        model = Book
        fields: ClassVar[list[str]] = [
            'id',
            'title',
            'author_id',
            'author',
            'total_copies',
            'available_copies',
            'isbn',
        ]

