from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.log_examiner,name="log_examiner"),
    path('check_error_404/',views.check_error_404,name="check_error_404")
]