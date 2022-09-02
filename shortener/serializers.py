from rest_framework import serializers
from shortener.models import (Url,)
from datetime import datetime
import uuid
from django.conf import settings

class UrlSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    user_id=serializers.IntegerField(write_only=True,required=False)
    

    class Meta:
        model=Url
        fields=('id','original_url','short_url','user','user_id')

  
   
    def create(self, validated_data):
        original_url=validated_data.pop('original_url')
        current_user = self.context['request'].user
        user=Url.objects.create(user=current_user,original_url=original_url)
        return user
        
    



















