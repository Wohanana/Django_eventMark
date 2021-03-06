from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    c_time = models.DateTimeField(auto_now_add=True)
    is_headman=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_group=models.BooleanField(default=False)
    group=models.CharField(max_length=2,default='0')
    objects = models.Manager()

    def __str__(self):
        return self.username

    class meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

class Headman(models.Model):
    username = models.CharField(max_length = 20)
    is_headman=models.BooleanField(default=False)
    group=models.CharField(max_length=2,default='0')
    objects = models.Manager()
    
    def __str__(self):
        return self.username