from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('add-place', views.index, name="add-place"),
    url(r'^(?P<place_id>[0-9]+)/$', views.place_details, name="place-details"),
]