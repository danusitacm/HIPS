from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_verification, name='file_verification'),
    path('create_hashes/', views.create_hashes, name='create_hashes'),
    path('check_files/', views.check_files, name='check_files'),
    path('create_backup/', views.create_backup, name='check_files'),
]
