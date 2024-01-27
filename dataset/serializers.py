from rest_framework import serializers

from dataset.models import InsuranceData


class InsuranceSerializerCover(serializers.ModelSerializer):

    class Meta:
        model = InsuranceData
        fields = ['iin']


class InsuranceSerializerDetail(serializers.ModelSerializer):

    class Meta:
        model = InsuranceData
        fields = "__all__"


