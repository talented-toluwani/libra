from typing import ClassVar

from rest_framework import viewsets

from .filters import BookFilter
from .models import Author, Book
from .permissions import IsLibrarianOrReadOnly
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes:ClassVar = [IsLibrarianOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    permission_classes:ClassVar = [IsLibrarianOrReadOnly]
        
    