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

def past_days_images(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_of_day)

    return render(request, 'all_gallery/past-images.html', {"date": date})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_images_name(search_term)
        message = f"{search_term}"

        return render(request, 'all_gallery/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_gallery/search.html',{"message":message})

   
def get_images(request,post_id):
    try:
      post = Images.objects.get(id = post.id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all_gallery/single_image.html", {"post":post})