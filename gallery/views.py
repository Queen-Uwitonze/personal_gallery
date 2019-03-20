from django.shortcuts import render,redirect
from django.http  import Http404
import datetime as dt
from .models import Images,Category,Location

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def images_of_day(request):
    gallery = Images.objects.all()
    date = dt.date.today()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    return render(request, 'all_gallery/today-images.html',{'gallery':gallery}, {"date": date})


def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_categories = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_gallery/search.html',{"message":message,"images": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_gallery/search.html',{"message":message})     

   
def single_images(request,image_id):
    images = Images.objects.get(id=image_id)
    return render(request,"all_gallery/single_image.html", {"images":images})

