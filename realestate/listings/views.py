from django.shortcuts import render
from .models import House

# Create your views here.
def index(request):
    try:
        if(int(request.GET['bedroom']) > 0):
            houses = House.objects.filter(bedroom=request.GET['bedroom']) 
        else:
            houses = House.objects.all()
    except:
        # Get all houses
        houses = House.objects.all() 
    context={'houses': houses}
    # render page from "templates/index.html"
    return render(request,"index.html",context)
