from django.db import models


class InsuranceData(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    children = models.IntegerField()
    smoker = models.CharField(max_length=10)
    region = models.CharField(max_length=20)
    charges = models.DecimalField(max_digits=10, decimal_places=2)
    iin = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.iin} - {self.age} - {self.sex}"
