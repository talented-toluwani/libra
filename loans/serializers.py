from django.utils import timezone
from rest_framework import serializers

from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    days_overdue = serializers.SerializerMethodField()
    class Meta:
        model = Loan
        fields = '__all__'

    def get_days_overdue(self, obj):

        """
         if obj.returned_at:
            reference_date = obj.returned_at
        else:
            reference_date = timezone.now()  this is the if condition, but the ternary codition below
        """
        reference_date = obj.returned_at if obj.returned_at else timezone.now()

        if reference_date <= obj.due_at:
            return 0

        overdue_delta = reference_date - obj.due_at
        return overdue_delta.days
    
    def validate(self, data):
        book= data.get('book')
  
        if book and not book.available_copies:
            raise serializers.ValidationError(
                {"book": "This book has no available copies."}
            )

        return  data
