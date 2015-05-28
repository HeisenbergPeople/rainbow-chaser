#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

# -*- coding: utf-8 -*-

from django.forms import ModelForm

from sensor.dummy.models.dummy_event import DummyEvent


class DummyEventUploadForm(ModelForm):

    class Meta:
        model = DummyEvent
        fields = ('sensor', 'datetime', 'value')