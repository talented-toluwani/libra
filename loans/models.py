from django.conf import settings
from django.db import models

from catalog.models import Book


class Loan(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    borrowed_at=models.DateTimeField(auto_now_add=True)
    due_at=models.DateTimeField()
    returned_at=models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.book} borrowed by {self.user}"