from django.urls import path, include
from . import views

urlpatterns = [
    path('file_verification/',views.file_verification,name="file_verification"),
    path('file_verification/create_hashes',views.create_hashes,name="create_hashes"),
    path('file_verification/check_files',views.check_files,name="check_files")
]