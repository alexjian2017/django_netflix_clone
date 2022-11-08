from django.contrib import admin
from django.urls import path
from .views import Home

app_name = 'core'
urlpatterns = [
    path('', Home.as_view()),
]