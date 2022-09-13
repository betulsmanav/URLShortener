from rest_framework import generics,permissions
from rest_framework.generics import get_object_or_404
from django.shortcuts import redirect
from django.views import View
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
    UrlSerializer,
    LogSerializer
    )
from .permission import IsUserRead
from shortener.models import (Url,Log)





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

    # ? aeralizers da hallettik buna gerek kalmadi
    # def perform_create(self, serializer):
    #     current_user=self.request.user
    #     serializer.save(user=current_user)
    
class UrlRedirect(View):
    def get(self,request,shortener,*args, **kwargs):
        shortener=settings.HOST_URL + "/" + self.kwargs['shortener']
        redirect_url=Url.objects.filter(short_url=shortener).first().original_url
    
        return redirect(redirect_url)            

        


    


    
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
    







from ua_parser import user_agent_parser
import pprint
pp = pprint.PrettyPrinter(indent=4)
from django.http import HttpResponse
def data(request):

    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    print("====================",user_agent)

    parsed_string = user_agent_parser.Parse(user_agent)
    browser=user_agent_parser.ParseUserAgent(user_agent)['family']
    print("====================",browser)
    pp.pprint(parsed_string)


    msg = f'''
        <html>
        Path: {path}<br>
        Scheme: {scheme}<br>
        Method: {method}<br>
        Address: {address}<br>
        User agent: {user_agent}<br>
        parse: {parsed_string}
        </html>
        '''

    return HttpResponse(msg, content_type='text/html', charset='utf-8')


