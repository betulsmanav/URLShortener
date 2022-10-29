from django.db import models
from django.contrib.auth.models import User
import uuid
from ua_parser import user_agent_parser
import pprint
pp = pprint.PrettyPrinter(indent=4)

class Url(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=None, null=True, editable=False)
    original_url=models.URLField(max_length=1000)
    short_url=models.URLField(max_length=30,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user,self.original_url}'

    class Meta:
        unique_together = ('original_url', 'short_url')
   


class Log(models.Model):
    url = models.ForeignKey(Url,on_delete=models.CASCADE, default=None, null=True, editable=False)
    create_user = models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    server_name = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    device_brand = models.CharField(max_length=100)
    device_family = models.CharField(max_length=100)
    device_model = models.CharField(max_length=100)
    

        


    def log_data(request):
        
        user = request.META['REMOTE_USER']
        address = request.META['REMOTE_ADDR']
        server_name=request.META['SERVER_NAME']
        ua_string = request.META['HTTP_USER_AGENT']
        browser=user_agent_parser.ParseUserAgent(ua_string)['family']
        operating_sistem = user_agent_parser.ParseOS(ua_string)['family']
        device_brand = user_agent_parser.ParseDevice(ua_string)['brand']
        device_family = user_agent_parser.ParseDevice(ua_string)['family']
        device_model = user_agent_parser.ParseDevice(ua_string)['model']
     

        log = Log(
            create_user=user,
            address=address,
            server_name=server_name,
            browser=browser,
            os=operating_sistem,
            device_brand=device_brand,
            device_family=device_family,
            device_model=device_model,
        )

        return log

    def save(self,*args, **kwargs):
        log=self.log_data()
        self.address=log.address
        self.browser=log.browser
        self.operating_sistem=log.operating_sistem
        self.device_brand=log.device_brand
        self.device_family=log.device_family
        self.device_model=log.device_model
       
        return super().save(*args, **kwargs)



    


















        
# from ua_parser import user_agent_parser
    # def save(self,*args,**kwargs):
    #     # user_agent = request.META['HTTP_USER_AGENT']
    #     # parsed_string = user_agent_parser.PrettyUserAgent(user_agent)
    #     # self.browser=parsed_string
        
    #     return super().save(*args,**kwargs)
     


