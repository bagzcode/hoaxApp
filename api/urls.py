from django.urls import path, include
from rest_framework import routers
from api.views import HoaxTest

urlpatterns = [
    path('hoax-test/', HoaxTest.as_view(), name="hoax-test"),
]
