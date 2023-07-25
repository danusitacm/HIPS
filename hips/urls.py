"""
URL configuration for hips project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('home/', views.home, name='home'),
    path('file_verification/', include('file_verification.urls')),
    path('user_connected/', include('user_connected.urls')),
    path('cron/', include('cron_jobs_examiner.urls')),
    path('sniffer_detection/', include('sniffer_detection.urls')),
    path('mail_queue_checker/', include('mail_queue_checker.urls')),
    path('tmp_directory_checker/', include('tmp_directory_checker.urls')),
    path('high_consumed_resources/', include('high_consumed_resources.urls')),
    path('log_examiner/', include('log_examiner.urls')),
]
