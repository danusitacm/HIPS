from django.urls import path, include
from . import views

urlpatterns = [
    path('tmp_directory_check/',views.check_tmp_files,name="tmp_directory_check"),
    path('tmp_directory_check/check_temp_ps',views.check_tmp_ps,name="check_temp_ps"),
    path('tmp_directory_check/check_tmp_extension',views.check_tmp_extension,name="check_tmp_extension"),
    path('tmp_directory_check/check_tmp_script',views.check_tmp_script,name="check_tmp_script"),
]