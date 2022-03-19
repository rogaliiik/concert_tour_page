from django.forms import ModelForm, TextInput
from .models import Subscriber


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

        widgets = {
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email to subscribe'
            })
        }
