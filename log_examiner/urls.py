from django.urls import path, include
from . import views

urlpatterns = [
    path('log_examiner/',views.log_examiner,name="log_examiner"),
]