from django.shortcuts import render
from .models import Students

# Create your views here.


def index(request):
    return render(request, 'students/index.html')
