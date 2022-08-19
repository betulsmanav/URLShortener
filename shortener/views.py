from rest_framework import generics,permissions
from django.shortcuts import redirect
from django.views import View
from django.conf import settings
from .serializers import (
    UrlSerializer,
    )
from shortener.models import Url


class UrlListAPIView(generics.ListAPIView):
    queryset=Url.objects.all()
    serializer_class=UrlSerializer


class UrlCreateAPIView(generics.CreateAPIView):
    serializer_class=UrlSerializer

class UrlRedirect(View):
    def get(self,request,shortener,*args, **kwargs):
        shortener=settings.HOST_URL + "/" + self.kwargs['shortener']
        redirect_url=Url.objects.filter(short_url=shortener).first().original_url
        return redirect(redirect_url)










# class UrlModelView(viewsets.ModelViewSet):

#     queryset=Url.objects.all()
#     serializer_class=UrlSerializer
#     permission_classes=(permissions.IsAuthenticated,)
#     lookup_field='short_url'




    



   