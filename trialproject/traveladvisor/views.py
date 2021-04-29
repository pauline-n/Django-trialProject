from django.shortcuts import render
from django.http import HttpResponse
from .models import BookaTrip

# Create your views here.

def home(request):
    # return HttpResponse('Hello Trip Advisor')
    # below is to be able to get data from the databse on all the trips made/entered
    trips = BookaTrip.objects.all()
    # return render(request, 'home.html')
    return render(request, 'home.html', {'trips':trips})