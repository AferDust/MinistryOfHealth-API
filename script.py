import csv
import random
import os
import django
from django.db.models import Count

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MinistryOfHealth.settings')
django.setup()
from django.core.exceptions import ValidationError
from dataset.models import InsuranceData



import secrets

# Generate a secure random string token
def generate_token():
    return secrets.token_urlsafe(32)

# Example usage
API_KEY = generate_token()
print(API_KEY)

