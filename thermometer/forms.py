#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django import forms
from django.forms import ModelForm, Form
from models import Event

class EventFilterForm(Form):

    start_datetime = forms.CharField(label='From', max_length=100)
    end_datetime = forms.CharField(label='To', max_length=100)

    thermometer = forms.CharField(label='Thermometer', max_length=100)
