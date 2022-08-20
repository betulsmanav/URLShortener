from rest_framework import generics,permissions
from django.shortcuts import redirect
from django.views import View
from django.conf import settings
from .serializers import (
    UrlSerializer,
    # ListSerializer
    )
from shortener.models import Url


class UrlListAPIView(generics.ListAPIView):
    queryset=Url.objects.all()
    serializer_class=UrlSerializer
    permission_classes=(permissions.IsAuthenticated,)


class UrlCreateAPIView(generics.CreateAPIView):
    serializer_class=UrlSerializer
    permission_classes=(permissions.IsAuthenticated,)


class UrlRedirect(View):
    def get(self,request,shortener,*args, **kwargs):
        shortener=settings.HOST_URL + "/" + self.kwargs['shortener']
        redirect_url=Url.objects.filter(short_url=shortener).first().original_url
        return redirect(redirect_url)




# class ListCreateAPIView(generics.CreateAPIView):
#     serializer_class=ListSerializer
# class ListAPIView(generics.ListAPIView):
#     queryset=Url.objects.all()
#     serializer_class=ListSerializer
# class LinkRedirect(View):
#     def get(self,request,shortener_link,*args, **kwargs):
#         shortener_link=settings.HOST_URL + "/" + self.kwargs['shortener_link']
#         redirect_link=Url.objects.filter(short_link=shortener_link).first().original_link
#         return redirect(redirect_link)










