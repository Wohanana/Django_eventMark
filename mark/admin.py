from django.contrib import admin

# Register your models here.
from .models import Txt,Marktxt
admin.site.register(Txt)
admin.site.register(Marktxt)
