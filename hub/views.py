from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'hub/dashboard.html')


def overview(request):
    return render(request, 'hub/overview.html')


def networksettings(request):
    return render(request, 'hub/networksettings.html')


def idssettings(request):
    return render(request, 'hub/idssettings.html')


def scan(request):
    return render(request, 'hub/scan.html')


def idsresults(request):
    return render(request, 'hub/ids.html')


def dns(request):
    return render(request, 'hub/dns.html')