from django.urls import path
from psMain_app import views as psMain_app_views

urlpatterns = [
    path('', psMain_app_views.index),
]
