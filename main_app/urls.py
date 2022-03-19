from django.urls import path
from .views import MainView, TourView, redirect_view


urlpatterns = [
    path('', redirect_view, name='redirect_view'),
    path('fest/', MainView.as_view(), name='main_view'),
    path('tour/', TourView.as_view(), name='tour_view'),

]