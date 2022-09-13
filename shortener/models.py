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
    # create_user = models.ForeignKey(User,on_delete=models.CASCADE, default=None, null=True, editable=False)
    # timestamp=models.DateTimeField(auto_now_add=True)
    browser = models.CharField(max_length=100)
    

        


    def gelen(request):
        # url=
        # path = request.path
        # scheme = request.scheme
        # method = request.method
        # address = request.META['REMOTE_ADDR']
        user_agent = request.META['HTTP_USER_AGENT']
        parsed_string = user_agent_parser.Parse(user_agent)
        browser=user_agent_parser.ParseUserAgent(user_agent)['family']
        print("====================",browser)
        print("+++++++++++",parsed_string)

        log = Log(
            browser=browser
        )

        return log

    def save(self,*args, **kwargs):
        browser=self.gelen()
        self.browser=browser
       
        return super().save(*args, **kwargs)



    


















        
# from ua_parser import user_agent_parser
    # def save(self,*args,**kwargs):
    #     # user_agent = request.META['HTTP_USER_AGENT']
    #     # parsed_string = user_agent_parser.PrettyUserAgent(user_agent)
    #     # self.browser=parsed_string
        
    #     return super().save(*args,**kwargs)
     


