from django.shortcuts import render
from .models import paintings

# Create your views here.
def index(request):
    dict_paintings={
        'paintings': paintings.objects.all()
    }
    return render (request, "index.html",dict_paintings)
