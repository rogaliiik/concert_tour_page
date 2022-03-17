from django.urls import path
from .views import main_view, redirect_view


urlpatterns = [
    path('', redirect_view, name='redirect_view'),
    path('fest/', main_view, name='main_view'),
]