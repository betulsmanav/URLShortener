from django.urls import path,include
from .views import (
    UrlListAPIView,
    UrlCreateAPIView,
    
    )

urlpatterns = [ 
    path('',UrlListAPIView.as_view()) ,
    path('create/',UrlCreateAPIView.as_view()) ,

   

]












