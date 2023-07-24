from django.shortcuts import render

# Create your views here.
def sniffer_detection(request):
    return render(request, "sniffer_verification.html")
    
def check_sniffer(request):
    return render(request, "check_sniffer_temp.html")

def check_promiscuous(request):
    return render(request,"check_promisc_temp.html" )