from django.db import models
from account.models import User
import django.utils.timezone as timezone

class Txt(models.Model):
    group = models.CharField(max_length=3,default='0')
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Marktxt(models.Model):
    marktxt_type = models.CharField(max_length=50,default='')
    start = models.CharField(max_length=10,default='')
    end = models.CharField(max_length=10,default='')
    text = models.CharField(max_length=100,default='')
    
    user =models.CharField(max_length=100,default='')
    user_group=models.CharField(max_length=3,default='0')
    txt =models.CharField(max_length=100,default='')
    is_finished=models.BooleanField(default=False)
    objects = models.Manager()

    def  __str__(self):
        return  self.marktxt_type
