from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import MemberSerializer
from .serializers import PeriodSerializer
from rest_framework import status


from .models import Member

from .models import Period

# Create your views here.
class MemberListView (APIView):
    def get (self, request):
        Members= Member.objects.all()
        serializer = MemberSerializer(Members, many=True)
        return Response(serializer.data)
    def post(self, request):

        serializer= MemberSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PeriodListView (APIView):
    def get (self, request):
        Periods= Period.objects.all ()
        serializer = PeriodSerializer(Periods, many=True)
        return Response(serializer.data)
    #Deserialization(JSON TO MODEL)
    def post(self, request):

        serializer= PeriodSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









