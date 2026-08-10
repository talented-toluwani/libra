from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey
    total_copies = models.IntegerField()
    availables_copies = models.IntegerField()
    isbn = models.CharField( max_length=17, unique=True, blank= True, null=True)

    def __str__(self) -> str:
        return f"{self.title} is written by {self.author}"


