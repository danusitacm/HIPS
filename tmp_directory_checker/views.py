from django.shortcuts import render
from function.utils import execute_process,kill_process
import subprocess
import os
# Create your views here.
def check_tmp_files(request):
        return render(request, "tmp_directory_check.html")

def check_tmp_extension(request):
        return render(request, "check_tmp_extension.html")

def check_tmp_script(request):
        return render(request, "check_tmp_script.html")
