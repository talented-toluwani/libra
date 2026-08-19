from django.urls import path

from .views import LoanListCreateAPIView, LoanRetrieveUpdateAPIView

urlpatterns = [
    path('loans/', LoanListCreateAPIView.as_view(), name='loan-list'),

    path('loans/<int:pk>/', LoanRetrieveUpdateAPIView.as_view(), name='loan-detail')
]

