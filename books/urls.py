from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router =DefaultRouter()
router.register(r'books', views.BookViewSet,"books")

urlpatterns = [
    path('',include(router.urls)),
    path('library/', views.library),
]
