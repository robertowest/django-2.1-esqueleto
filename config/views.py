from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'pages/home.html')


def login(request):
    return render(request, 'users/login.html')


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'users/profile.html')
