from Persons import views
from django.urls import path

urlpatterns=[
    path('list_people/', views.list_people, name='list people')
]