from rest_framework import serializers

from ads.models import Ads

class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ['id', 'name', 'link', 'banner']