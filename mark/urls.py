from django.urls import path
from . import views

urlpatterns = [
    path('txtlist',views.txt_list),
    path('admin',views.admin),
    path('chargeman/<k>',views.charge,name='charge'),
    path('txt/<int:txt_id>/',views.txt_detail),
    path('txt/<int:txt_id>/edit',views.txt_edit),
    path('txt/edit',views.group_edit),
    path('refer/',views.txt_refer),
    path('<int:is_finished>/<int:txt_id>',views.finish),
    path('delete/',views.txt_delete),
    path('mark_detail/<int:txt_id>',views.mark_detail),
    path('download/',views.txt_download),
    path('upload/',views.txt_upload),
]