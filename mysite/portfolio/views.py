from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from Top_Skills.dash_app import *


def index(request):
    return render(request, 'portfolio/index.html')

def snake(request):
    return render(request, 'portfolio/snake.html')

def flashcard(request):
    return render(request, 'portfolio/flashcard.html')