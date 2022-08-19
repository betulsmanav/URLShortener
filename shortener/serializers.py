from rest_framework import serializers
from shortener.models import (
    Url,
    # UrlList
    )

class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model=Url
        fields=('id','original_url','short_url')



# class ListSerializer(serializers.ModelSerializer):
#     original_link=serializers.ListField(
#         child=serializers.CharField(),initial = []
#     )
#     short_link=serializers.ListField(
#         child=serializers.CharField(),initial = []
#     )
#     class Meta:
#         model=UrlList
#         fields=('original_link','short_link')

















