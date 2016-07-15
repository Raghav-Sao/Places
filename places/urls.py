from django.conf.urls import include, url
import views

urlpatterns = [
	url('add-place', views.add_place, name="add-place"),
    url(r'^(?P<place_id>[0-9]+)/$', views.place_details, name="place-details"),
    url('^$', views.places, name="places"),
]