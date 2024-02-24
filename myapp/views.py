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
    battery_images = [
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/1.jpg', 'description': 'Battery Image 1'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/2.jpg', 'description': 'Battery Image 2'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/3.jpg', 'description': 'Battery Image 3'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/4.jpg', 'description': 'Battery Image 4'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/5.jpg', 'description': 'Battery Image 5'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/6.jpg', 'description': 'Battery Image 6'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/7.jpg', 'description': 'Battery Image 7'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/8.jpg', 'description': 'Battery Image 8'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/9.jpg', 'description': 'Battery Image 9'}
    ]

    return render(request, 'projects.html', {'battery_images': battery_images})

