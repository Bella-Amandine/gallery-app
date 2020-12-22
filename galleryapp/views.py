from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    all_images = Image.get_all_image
    return render(request, 'index.html', {"images": all_images})