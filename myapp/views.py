from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def profile(request):
    return render(request, "profile.html")

def shader_background_view(request):
    return render(request, 'shader_background.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')
