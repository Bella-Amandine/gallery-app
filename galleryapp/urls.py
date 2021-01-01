from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.index,name='home'),
    url(r'^all/images/',views.get_all_images, name='all_images'),
    url(r'^search/category/',views.search_by_category_results, name='search_cat_results'),
    url(r'^search/location/',views.search_by_location_results, name='search_loc_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)