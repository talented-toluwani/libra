from rest_framework import generics

from .models import Loan
from .serializers import LoanSerializer


class LoanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer()

class LoanRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer