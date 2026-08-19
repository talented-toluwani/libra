from typing import ClassVar

import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
   
    available: ClassVar[django_filters.BooleanFilter] = (
        django_filters.BooleanFilter(method="filter_available")
    )

    class Meta:
        model = Book
        fields: ClassVar[list[str]] = ["author", "available"]

    def filter_available(self, queryset, name, value):
        if value:
            return queryset.filter(available_copies__gt=0)
        return queryset.filter(available_copies=0)