from django.contrib import admin
from django.urls import path
from .views import TextConverter
urlpatterns = [
    path('converter/', TextConverter.as_view(), name="text_converter"),
]
