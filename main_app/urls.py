from django.urls import path
from .views import MainView, redirect_view


urlpatterns = [
    path('', redirect_view, name='redirect_view'),
    path('fest/', MainView.as_view(), name='main_view'),
]