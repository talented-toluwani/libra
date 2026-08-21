from typing import ClassVar

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Loan
from .permissions import IsOwnerOrLibrarian
from .serializers import LoanSerializer


class LoanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer()
    permission_classes:ClassVar =[IsAuthenticated]

class LoanRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes:ClassVar = [IsOwnerOrLibrarian]
