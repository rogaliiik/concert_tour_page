from django.contrib import admin
from .models import Subscriber, Concert


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'verified']


@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ['id', 'arena', 'date', 'city' ]
