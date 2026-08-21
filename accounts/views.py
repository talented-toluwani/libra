from typing import ClassVar

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import CustomUser
from .serializers import RegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes:ClassVar = [AllowAny]
