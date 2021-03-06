from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout),
    path('join/',views.join),
    path('head/',views.head),
    path('head_confirm/',views.head_confirm),
]