from django.urls import path,include
from .views import (
    UrlListAPIView,
    UrlDetailAPIView,
    UrlCreateAPIView,
    LogCreateAPIView,
    # LogListAPIView,
    data
    )

urlpatterns = [ 
    path('',UrlListAPIView.as_view()) ,
    path('url/<str:pk>',UrlDetailAPIView.as_view(),name='url-detail') ,
    path('create/',UrlCreateAPIView.as_view()) ,
    
    path('url/<str:url_pk>/log',LogCreateAPIView.as_view(),name='log') ,

    # path('list',LogListAPIView.as_view()) ,
    path('data/', data, name='data'),
   

]












