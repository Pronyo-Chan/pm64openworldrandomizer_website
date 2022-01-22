from django.urls import path, include

from rest_framework import routers

from .views import RandomizerViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', RandomizerViewSet, basename='randomizer')

urlpatterns = [
    path('', include(router.urls))
]