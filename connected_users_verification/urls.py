from django.urls import path
from . import views

urlpatterns = [
    path('', views.connected_users_view, name='connected_users'),
]