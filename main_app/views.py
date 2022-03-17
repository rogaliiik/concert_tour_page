from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView


def redirect_view(request):
    return redirect('/fest')


def main_view(request):
    return render(request, 'main.html')
