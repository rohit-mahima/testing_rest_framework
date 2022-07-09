from urllib.parse import urlparse
from django import views
from django.urls import path
from .views import tools
urlpatterns = [
    path('listtools/',tools.list_tools)
]
