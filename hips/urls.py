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
    path('',views.index, name='index'),
    path('',include('file_verification.urls')),
    path('',include('user_connected.urls')),
    path('',include('cron_jobs_examiner.urls')),
    path('',include('sniffer_detection.urls')),
    path('',include('mail_queue_checker.urls')),
    path('',include('tmp_directory_checker.urls')),
    path('',include('high_consumed_resources.urls'))
]
