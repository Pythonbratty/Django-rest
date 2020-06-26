from timezone_field import TimeZoneField
from django.db import models

# Create your models here.


class Member (models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    real_name = models.CharField(max_length=60)
    tz = TimeZoneField(default='Europe/London')


class Period (models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()



