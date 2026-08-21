from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Loan


@receiver(post_save, sender=Loan)
def loan_update(sender, instance, created, **kwargs):
    book = instance.book

    if created:
        book.available_copies -= 1
        book.save()
    elif instance.returned_at:
        book.available_copies += 1
        book.save()