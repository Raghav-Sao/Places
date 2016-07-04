from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('add-place', views.index, name="add-place"),
]