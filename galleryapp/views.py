from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Category, Location
import pyperclip

# Create your views here.
def index(request):
    all_locations = Location.get_all_location()
    return render(request, 'index.html', {"locations": all_locations})

def get_all_images(request):
    all_images = Image.get_all_image()
    return render(request, 'all-images/all-images.html', {"images": all_images})

def get_all_images_by_location(request, location_name):
    all_images_by_loc = Image.filter_by_location(location_name)
    return render(request, 'all-images/all-images-by-loc.html', {"images" : all_images_by_loc})

def search_by_category_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html', {"message": message})

def search_by_location_results(request):

    if 'location' in request.GET and request.GET["location"]:

        search_term = request.GET.get("location")
        searched_images = Image.filter_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html', {"message": message})


def copy_image_link(request, image_id):
    image_found = Image.get_image_by_id(image_id)
    pyperclip.copy(image_found.image)
