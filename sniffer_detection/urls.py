from django.urls import path, include
from . import views

urlpatterns = [
    path('sniffer_detection/',views.sniffer_detection,name="sniffer_detection"),
    path('sniffer_detection/check_sniffer/',views.check_sniffer,name="check_sniffer"),
    path('sniffer_detection/check_promiscuous/',views.check_promiscuous,name="check_promiscuous")
]