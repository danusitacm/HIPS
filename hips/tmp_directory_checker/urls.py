from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.check_tmp_files,name="tmp_directory_check"),
    path('check_tmp_extension/',views.check_tmp_extension,name="check_tmp_extension"),
    path('check_tmp_script/',views.check_tmp_script,name="check_tmp_script"),
]