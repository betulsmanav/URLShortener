from django.db import models
from django.contrib.auth.models import User

import uuid
from django.conf import settings
# Create your models here.

class Url(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=None, null=True, editable=False)
    original_url=models.URLField(max_length=1000)
    short_url=models.URLField(max_length=30,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user,self.original_url}'

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





