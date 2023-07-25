from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.high_consumed_resources,name="high_consumed_resources"),
    path('check_ram/',views.check_ram,name="check_ram"),
    path('check_cpu/',views.check_cpu,name="check_cpu"),
    
]