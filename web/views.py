from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import sampleweb
from .serializers import samplewebSerailizers
from rest_framework.decorators import api_view


# Create your views here.
#class based view
class saview(APIView):

    def get(self,request):
        sampleviewdb=sampleweb.objects.all()
        serial=samplewebSerailizers(sampleviewdb,many=True)
        return Response(serial.data)

    def post(self,request):
        pass


@api_view(['GET'])
def apioverview(request):
    api_url ={
        'List':'somy',
        'Detail':'task'
    }
    return Response(api_url)

@api_view(['GET'])
def modelserial(request):
    all_data = sampleweb.objects.all()
    serial_data = samplewebSerailizers(all_data,many=True)
    return Response(serial_data.data)

#to put data in model
@api_view(['POST'])
def put_data(request):
    serial_data = samplewebSerailizers(data=request.data)

    if serial_data.is_valid():
        serial_data.save()

    return Response(serial_data.data)

#to update the api data

@api_view(['POST'])
def update_data(request,pk):
    data= sampleweb.objects.get(id=pk)
    serial_data = samplewebSerailizers(instance=data, data=request.data)

    if serial_data.is_valid():
        serial_data.save()

    return Response(serial_data.data)


#delete the mehod

@api_view(['DELETE'])
def delete_data(request,pk):
    data= sampleweb.objects.get(id=pk)
    data.delete()


    return Response("Item delted")