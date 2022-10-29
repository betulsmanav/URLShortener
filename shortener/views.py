from rest_framework import generics,permissions,mixins
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from .permission import IsUserRead
from .serializers import (
    UrlSerializer,
    LogSerializer
    )
from .models import (
    Url,
    Log
    )


class LoggingView(LoggingMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    logging_methods = ['GET']
    model = Log
    def get(self, request):
        return Response('with logging')



















class UrlListAPIView(generics.ListAPIView):
    serializer_class=UrlSerializer
    permission_classes= (permissions.IsAuthenticated,)

    def get_queryset(self):
        current_user=self.request.user
        admin = self.request.user.is_staff
        if current_user and admin:
            queryset=Url.objects.all()
            return queryset
        elif current_user:
            queryset=Url.objects.filter(user=current_user)
            return queryset

class UrlDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Url.objects.all()
    serializer_class=UrlSerializer
    permission_classes=(permissions.IsAuthenticated,IsUserRead,)

class UrlCreateAPIView(generics.CreateAPIView):
    queryset=Url.objects.all
    serializer_class=UrlSerializer
    permission_classes=(permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,many=isinstance(request.data,(list or dict)))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
# class UrlRedirect(View):
#     def get(self,request,shortener,*args, **kwargs):
#         shortener=settings.HOST_URL + "/" + self.kwargs['shortener']
#         redirect_url=Url.objects.filter(short_url=shortener).first()
#         print("====================================================================================")

#         print("********************************",redirect_url)
#         print("====================================================================================")

    
#         return redirect(redirect_url)            

        


    


    
class LogCreateAPIView(generics.CreateAPIView):
    queryset=Log.objects.all()
    serializer_class=LogSerializer
    permission_classes=(permissions.IsAuthenticated,IsUserRead,)

    def perform_create(self, serializer):
    # path('url/<str:url_pk>/log',LogCreateAPIView.as_view()) ,
        url_pk=self.kwargs.get('url_pk')
        url=get_object_or_404(Url,pk=url_pk)
        serializer.save(url=url)
    

class LogListAPIView(generics.ListAPIView):
    queryset=Log.objects.all()
    serializer_class=LogSerializer
    permission_classes=(permissions.IsAuthenticated,IsUserRead,)
    







from django.http import HttpResponse
from ua_parser import user_agent_parser
import pprint
pp = pprint.PrettyPrinter(indent=4)

def data(request):
    
    user = request.META['REMOTE_USER']

    path = request.path
    scheme = request.scheme
    method = request.method
    server_name = request.META['SERVER_NAME']
    IP_address = request.META['REMOTE_ADDR']
    ua_string = request.META['HTTP_USER_AGENT']
    
    parsed_string = user_agent_parser.ParseWithJSOverrides(ua_string)
    parsed_string = user_agent_parser.Parse(ua_string)
    browser=user_agent_parser.ParseUserAgent(ua_string)['family']
    operating_sistem = user_agent_parser.ParseOS(ua_string)['family']
    device_brand = user_agent_parser.ParseDevice(ua_string)['brand']
    device_family = user_agent_parser.ParseDevice(ua_string)['family']
    device_model = user_agent_parser.ParseDevice(ua_string)['model']
    print("====================================================================================")
    pp.pprint(parsed_string)
    print("====================================================================================")


    msg = f'''
        <html>
        user: {user}<br>
        Path: {path}<br>
        Scheme: {scheme}<br>
        Method: {method}<br>
        Address: {IP_address}<br>
        server_name: {server_name}<br>
        User agent: {ua_string}<br>
        browser: {browser}<br>
        operating_sistem: {operating_sistem}<br>
        device_brand: {device_brand}<br>
        device_family: {device_family}<br>
        device_model: {device_model}<br>
        
        </html>
        '''
        
    return HttpResponse(msg, content_type='text/html', charset='utf-8')


