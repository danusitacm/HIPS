from django.shortcuts import render

# Create your views here.
def check_tmp_files(request):
        return render(request, "tmp_directory_check.html")

def check_tmp_ps(request):
        return render(request, "check_tmp_ps.html")

def check_tmp_extension(request):
        return render(request, "check_tmp_extension.html")

def check_tmp_script(request):
        return render(request, "check_tmp_script.html")
