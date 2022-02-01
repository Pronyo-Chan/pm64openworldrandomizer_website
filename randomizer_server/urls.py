from django.urls import re_path 
from rest_framework import routers

from randomizer_server import views


urlpatterns = [
    re_path(r'^randomizer_settings/(?P<pk>\d+)/?$', views.get_randomizer_settings),
    re_path(r'^randomizer_settings/?$', views.post_randomizer_settings),
]