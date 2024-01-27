import csv
import random
import os
import django
from django.db.models import Count

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MinistryOfHealth.settings')
django.setup()
from django.core.exceptions import ValidationError
from dataset.models import InsuranceData



duplicates = (
    InsuranceData.objects.values('age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges', 'iin')  # list all fields that define a duplicate
    .annotate(count_id=Count('id'))
    .order_by()
    .filter(count_id__gt=1)
)

print(duplicates)

print(InsuranceData.objects.get(iin=65230198224))

for entry in duplicates:
    # Exclude the first occurrence from the queryset to delete
    (
        InsuranceData.objects.filter(**entry)
        .order_by('id')  # Order by 'id' or another unique field to keep the first record
        .exclude(id=InsuranceData.objects.filter(**entry).order_by('id').first().id)  # Exclude the first one
        .delete()
    )
