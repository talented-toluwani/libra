from typing import ClassVar

from django.db import models
from django.db.models import Q


class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    total_copies = models.PositiveIntegerField(default=0)
    available_copies = models.PositiveIntegerField(default=0)
    isbn = models.CharField( max_length=17,unique=True, null=True, blank= True)

    @property
    def is_availabe(self):
        return bool(self.available_copies)

    def __str__(self) -> str:
        return f"{self.title} is written by {self.author}"


    class Meta:
        constraints: ClassVar[list[models.BaseConstraint]]= [
            models.CheckConstraint(
            condition=Q(available_copies__lte=models.F("total_copies")),
            name="available_copies_lte_total_copies",
        ),
    ]

