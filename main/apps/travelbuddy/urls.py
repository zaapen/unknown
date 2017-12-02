from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^success$', views.success),
    url(r'^travels$', views.travels),
    url(r'^travels/add$', views.add),
    url(r'^create$', views.create_trip),
    url(r'^join/(?P<trip_id>\d+)$', views.join),
    url(r'^travels/destination/(?P<trip_id>\d+)$', views.show),
]