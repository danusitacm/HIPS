from django.urls import path, include
from . import views

urlpatterns = [
    path('high_consumed_resources/',views.high_consumed_resources,name="high_consumed_resources"),
    path('high_consumed_resources/check_ram',views.check_ram,name="check_ram"),
    path('high_consumed_resources/check_cpu',views.check_cpu,name="check_cpu"),
    
]