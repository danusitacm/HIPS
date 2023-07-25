from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.check_user_cron,name="cron"),
]