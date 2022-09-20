from django.shortcuts import render
from .models import House

# Create your views here.
def index(request):
    # Get all houses
    houses = House.objects.all() 
    context={'houses': houses}
    # render page from "templates/index.html"
    return render(request,"index.html",context)
