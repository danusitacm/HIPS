from django.urls import path, include
from . import views

urlpatterns = [
    path('mail_queue_checker/',views.check_queue_email_view,name="mail_queue_checker"),
]