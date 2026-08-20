from django.urls import path

from .views import RegisterAPIView

urlpatterns = [
    path('accounts/', RegisterAPIView.as_view(), name='create-account')
]
