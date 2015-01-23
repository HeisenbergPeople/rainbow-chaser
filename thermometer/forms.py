from django import forms
from django.forms import ModelForm, Form
from models import Event

class EventFilterForm(Form):

    start_datetime = forms.CharField(label='From', max_length=100)
    end_datetime = forms.CharField(label='To', max_length=100)

    thermometer = forms.CharField(label='Thermometer', max_length=100)
