from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.index,name='home'),
    url(r'^all/images/',views.get_all_images, name='all_images'),
    url(r'^all/images/([a-zA-Z]+)',views.get_all_images_by_location, name='all_images_by_loc'),
    url(r'^search/category/',views.search_by_category_results, name='search_cat_results'),
    url(r'^search/location/',views.search_by_location_results, name='search_loc_results'),
    url(r'^images/copy/(\d+)',views.copy_image_link, name='copy_image_link'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)