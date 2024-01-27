from django.urls import path, include
from rest_framework import routers

from dataset.views import RetrieveInsuranceDataReadonlyModelViewSet

insurance_router = routers.SimpleRouter()
insurance_router.register(r'insurances', RetrieveInsuranceDataReadonlyModelViewSet)

urlpatterns = [
    path('api/v1/', include(insurance_router.urls))
]