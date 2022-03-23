from django.urls import path
from .views import MainView, TourView, MerchView, redirect_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', redirect_view, name='redirect_view'),
    path('fest/', MainView.as_view(), name='main_view'),
    path('tour/', TourView.as_view(), name='tour_view'),
    path('merch/', MerchView.as_view(), name='merch_view'),
] 