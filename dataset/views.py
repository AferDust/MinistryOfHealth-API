from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dataset.models import InsuranceData
from dataset.serializers import InsuranceSerializer


class RetrieveInsuranceDataAPIView(APIView):

    def get(self, request, iin):
        try:
            instance = InsuranceData.objects.get(iin=iin)
            serializer = InsuranceSerializer(instance)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as exception:
            return Response({'message': str(exception)}, status=status.HTTP_400_BAD_REQUEST)
