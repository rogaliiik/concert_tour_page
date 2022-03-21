from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import SubscribeForm
from .models import Subscriber, Concert
from django.http import HttpResponse


def redirect_view(request):
    return redirect('/fest')


class MainView(View):
    def get(self, request):
        sub_form = SubscribeForm()
        context = {
            'subscribe_form': sub_form
        }
        return render(request, 'main.html', context=context)

    def post(self, request):
        sub_form = SubscribeForm(request.POST)
        if sub_form.is_valid():
            Subscriber.objects.create(**sub_form.cleaned_data)
            return HttpResponse('An email with information has been sent')
        else:
            return render(request, 'main.html', {'subscribe_form': sub_form})


class TourView(View):
    def get(self, request):
        concerts = Concert.objects.all()
        sub_form = SubscribeForm()
        context = {
            'subscribe_form': sub_form,
            'concerts': concerts
        }
        return render(request, 'tour.html', context=context)

    def post(self, request):
        sub_form = SubscribeForm(request.POST)
        concerts = Concert.objects.all()
        context = {
            'subscribe_form': sub_form,
            'concerts': concerts
        }
        if sub_form.is_valid():
            Subscriber.objects.create(**sub_form.cleaned_data)
            return HttpResponse('An email with information has been sent')
        else:
            return render(request, 'tour.html', context=context)
