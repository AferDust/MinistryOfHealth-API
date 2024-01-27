from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from dataset.models import InsuranceData
from dataset.serializers import (
    InsuranceSerializerCover,
    InsuranceSerializerDetail
)


class RetrieveInsuranceDataReadonlyModelViewSet(ReadOnlyModelViewSet):
    queryset = InsuranceData.objects.all()
    serializer_class = InsuranceSerializerCover
    lookup_field = 'iin'

    def get_serializer_class(self):
        if self.action == 'list':
            return super().get_serializer_class()
        else:
            return InsuranceSerializerDetail
