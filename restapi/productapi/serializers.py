from rest_framework import serializers
from .models import Member
from .models import Period

class MemberSerializer ( serializers.ModelSerializer):
    class Meta:
        model= Member
        fields =['id', 'real_name']
class PeriodSerializer ( serializers.ModelSerializer):
    class Meta:
        model= Period
        fields = ['id', 'start', 'end', 'member_id']



