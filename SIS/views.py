from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'SIS/index.html')


def login(request):
    return render(request, 'SIS/registration/login.html')
