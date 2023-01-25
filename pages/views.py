from django.shortcuts import render
from .models import teamMember

# Create your views here.

def home(request):
    team = teamMember.objects.all()
    data = {
        'team': team
    }
    return render(request, 'pages/home.html', data)

def about(request):
    team = teamMember.objects.all()
    data = {
        'team': team
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')