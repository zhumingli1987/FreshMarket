from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'userModule/index.html')


def login(request):
    return render(request, 'userModule/login.html')


def register(request):
    return render(request, 'userModule/register.html')

