from rest_framework import serializers
from shortener.models import (Url,Log)
from datetime import datetime
import uuid
from django.conf import settings

class UrlSerializer(serializers.ModelSerializer):
    detail=serializers.HyperlinkedIdentityField(view_name='url-detail')
    user=serializers.StringRelatedField()
    

    class Meta:
        model=Url
        fields=('detail','id','original_url','short_url','user','created_at','updated_at')

    def short(self):
        while True:
            uid=str(uuid.uuid4())[:6]
            new_url=settings.HOST_URL + "/" + uid

            if not Url.objects.filter(short_url=new_url).exists():
                break
        return new_url

    def create(self, validated_data):
        liste=self.context['request'].data
        original_url=validated_data.pop('original_url')
        short_url=validated_data.pop('short_url')
        current_user = self.context['request'].user

        if type(liste) == list:
            print("listlistlistlistlist")
            for q in liste:

                original_url=q["original_url"]
                if not short_url:
                        new_url=self.short()
                url=Url.objects.create(user=current_user,original_url=original_url,short_url=new_url)
            return url

        elif type(liste) == dict:
            print("dictdictdictdictdictdictdict")
            if not short_url:
                new_url=self.short()
                url=Url.objects.create(user=current_user,original_url=original_url,short_url=new_url)
            return url
    
class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Log
        fields='__all__'

   















