from rest_framework import serializers
from shortener.models import Url

class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model=Url
        fields=('id','original_url','short_url')














# import uuid
    # def create(self,validated_data):
    #     uid=str(uuid.uuid4())[:5]
    #     link=Url.objects.create(**validated_data,short_url=uid)
    #     link.save()
    #     return link


