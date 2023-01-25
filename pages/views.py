from django.shortcuts import render
from .models import teamMember
from cars.models import Car

# Create your views here.

def home(request):
    team = teamMember.objects.all()
    all_cars = Car.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'team': team,
        'all_cars': all_cars,
        'featured_cars': featured_cars,
        
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