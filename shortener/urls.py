from django.urls import path,include
from .views import (
    UrlListAPIView,
    UrlCreateAPIView,
    UrlRedirect
    )

urlpatterns = [ 
    path('',UrlListAPIView.as_view()) ,
    path('create/',UrlCreateAPIView.as_view()) ,
    path('vv/',UrlRedirect.as_view()) ,

]












# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('urls', UrlModelView, basename='url')



# urlpatterns = [ 
#     path('', include(router.urls)),

# ]




# urlpatterns = router.urls
# router.register('urls', UrlModelView, basename='url')

