from django.db import models

import uuid
from django.conf import settings
# Create your models here.
from django.contrib.postgres.fields import ArrayField

class Url(models.Model):
    original_url=models.URLField(max_length=1000)
    short_url=models.URLField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.original_url

    def short(self):
        while True:
            uid=str(uuid.uuid4())[:6]
            new_url=settings.HOST_URL + "/" + uid

            if not Url.objects.filter(short_url=new_url).exists():
                break
        return new_url

    def save(self,*args,**kwargs):
        if not self.short_url:
            new_url=self.short()
            self.short_url=new_url
        return super().save(*args,**kwargs)
    class Meta:
        unique_together = ('original_url', 'short_url')




# class UrlList(models.Model):

#     original_link=ArrayField(
#         models.CharField(max_length=1000),default=list,size=8
#     )
#     short_link=ArrayField(
#         models.CharField(max_length=1000),default=list,size=8
#     )
