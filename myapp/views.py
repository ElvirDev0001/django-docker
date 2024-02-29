from django.shortcuts import render, HttpResponse
from .models import TodoItem
from django.shortcuts import render
from datetime import datetime, timedelta

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
    # Function to generate dates every 3 days starting from a specific date
    def generate_dates(start_date, end_date):
        date_list = []
        current_date = datetime.strptime(start_date, '%d%m%y')
        end_date_dt = datetime.strptime(end_date, '%d%m%y')
        while current_date <= end_date_dt:
            date_list.append(current_date.strftime('%d%m%y'))
            current_date += timedelta(days=3)
        return date_list

    # Generate dates from '290224' to the end of the year '311224'
    schuman_dates = generate_dates('280224', '311224')

    # Generate schuman_images list using the generated dates
    schuman_images = [
        {'url': f'https://storage.googleapis.com/bucketforimages666/schuman/{date}.jpg', 'description': f'schuman Image', 'date': date}
        for date in schuman_dates
    ]

    # Current UTC date and time
    current_utc_datetime = datetime.utcnow()

    # Function to parse image dates and compare with current date
    def image_should_be_displayed(image_date_str):
        image_date = datetime.strptime(image_date_str, '%d%m%y')
        return current_utc_datetime.date() >= image_date.date()

    # Filter images to include only those that should currently be displayed
    displayed_schuman_images = [img for img in schuman_images if image_should_be_displayed(img['date'])]
    battery_images = [
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/1.jpg', 'description': 'Battery Image 1'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/2.jpg', 'description': 'Battery Image 2'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/3.jpg', 'description': 'Battery Image 3'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/4.jpg', 'description': 'Battery Image 4'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/5.jpg', 'description': 'Battery Image 5'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/6.jpg', 'description': 'Battery Image 6'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/7.jpg', 'description': 'Battery Image 7'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/8.jpg', 'description': 'Battery Image 8'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/9.jpg', 'description': 'Battery Image 9'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/10.jpg', 'description': 'Battery Image 10'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/battery/11.jpg', 'description': 'Battery Image 11'},
    ]
    cnc_images = [
        {'url': 'https://storage.googleapis.com/bucketforimages666/cnc/1.jpg', 'description': 'cnc Image 1'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/cnc/2.jpg', 'description': 'cnc Image 2'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/cnc/3.jpg', 'description': 'cnc Image 3'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/cnc/4.jpg', 'description': 'cnc Image 4'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/cnc/5.jpg', 'description': 'cnc Image 5'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/cnc/6.jpg', 'description': 'cnc Image 6'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/cnc/7.gif', 'description': 'cnc Image 7'},
        {'url': 'https://storage.googleapis.com/bucketforimages666/cnc/8.gif', 'description': 'cnc Image 8'},
    ]

    # Pass the filtered list of schuman_images along with other image lists to your template
    return render(request, 'projects.html', {
        'battery_images': battery_images,
        'cnc_images': cnc_images,
        'schuman_images': displayed_schuman_images,
    })

