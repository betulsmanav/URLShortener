from django.urls import path,include
from .views import (
    UrlListAPIView,
    UrlCreateAPIView,
    # ListCreateAPIView,
    # ListAPIView
    )

urlpatterns = [ 
    path('',UrlListAPIView.as_view()) ,
    path('create/',UrlCreateAPIView.as_view()) ,

    # path('l',ListAPIView.as_view()) ,
    # path('list/',ListCreateAPIView.as_view()) ,

]












