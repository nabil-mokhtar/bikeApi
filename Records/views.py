from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from . import models
from . import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.
from .serializers import RentRecordsserializers


class RentRecordsview(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        rentRecords=models.RentRecords.objects.all()
        serializer=RentRecordsserializers(rentRecords,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=RentRecordsserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RentRecordDetails(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_record(self,qr):
        try:
            record= models.RentRecords.objects.get(bike=qr,status="1")
            return record
        except record.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
        except record.MultipleObjectsReturned:
            return Response(status=status.HTTP_409_CONFLICT)

    def get_recordByid(self, id):
        try:
            record = models.RentRecords.objects.get(id=id)
            return record
        except record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except record.MultipleObjectsReturned:
            return Response(status=status.HTTP_409_CONFLICT)

    def get(self,request,id):
        record=self.get_recordByid(self,id)
        serializer=RentRecordsserializers(record)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,qr,Sts):
        record=self.get_record(self,qr)
        serializer=RentRecordsserializers(record)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class RentRecordsview(viewsets.ModelViewSet):
#     queryset = models.RentRecords.objects.all()
#     serializer_class = serializers.RentRecordsserializers
#
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # def list(self, request):
    #     newest = self.get_queryset() # .order_by('created').last()
    #     # serializer = self.get_serializer_class()(newest)
    #     # return Response(serializer.data)
    #     return Response('newest')

    # def create(self, request):
    #     # new=models.RentRecords()
    #     # new.customer=models.RentUser(id=1)
    #     # new.bike= models.Bike(id=1)
    #     # new.starts= request.POST['starts']
    #     # new.ends= request.POST['ends']
    #     # new.status= request.POST['status'] #must be post-now
    #     # new.note= request.POST['note']
    #     # new.price= request.POST['price']
    #     # new.save()
    #     return Response('hello')

    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     p

class FixRecordsview(viewsets.ModelViewSet):
    queryset = models.FixRecords.objects.all()
    serializer_class = serializers.FixRecordsserializers


class SellBRecordview(viewsets.ModelViewSet):
    queryset = models.SellBRecord.objects.all()
    serializer_class = serializers.SellBRecordserializers


class SellARecordview(viewsets.ModelViewSet):
    queryset = models.SellARecord.objects.all()
    serializer_class = serializers.SellARecordserializers


class Noterecordview(viewsets.ModelViewSet):
    queryset = models.Noterecord.objects.all()
    serializer_class = serializers.Noterecordserializers
