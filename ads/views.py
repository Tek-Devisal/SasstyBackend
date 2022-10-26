from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ads.models import Ads
from ads.serializers import AdsSerializer

@api_view(['GET'])
def fetchAds(request, number_of_ads):
    try:
        ads = Ads.objects.all().order_by('?')[:number_of_ads]

    except Ads.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = AdsSerializer(ads, many=True)
        return Response(serializer.data)
