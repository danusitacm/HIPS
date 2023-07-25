from django.urls import path
from . import views

urlpatterns = [
    path('', views.sniffer_detection, name='sniffer_detection'),
    path('check_sniffer/', views.check_sniffer, name='check_sniffer'),
    path('check_promiscuous/', views.check_promiscuous, name='check_promiscuous'),
]
