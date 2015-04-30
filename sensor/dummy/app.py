#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

# -*- coding: utf-8 -*-

from django import apps

from sensor.core.views import DataUploadView
from sensor.dummy.models import DummySensor


class AppConfig(apps.AppConfig):

    name = 'sensor.dummy'
    verbose_name = 'Dummy Sensor'

    def ready(self):
        DataUploadView.register(DummySensor)