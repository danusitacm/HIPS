from django.urls import path, include
from . import views

urlpatterns = [
    path('user_connected/',views.check_user_connected,name="user_connected"),
]