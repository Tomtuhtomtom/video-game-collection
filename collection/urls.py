from django.urls import path
from collection import views

urlpatterns = [
    path('', views.api_root),
]