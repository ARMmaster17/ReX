from django.urls import include, path
from . import views

urlpatterns = [
  path('trigger', views.trigger)
]