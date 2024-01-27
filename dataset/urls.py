from django.contrib import admin
from django.urls import path, include

from dataset.views import RetrieveInsuranceDataAPIView


urlpatterns = [
    path('insurance/<str:iin>/', RetrieveInsuranceDataAPIView.as_view())
]