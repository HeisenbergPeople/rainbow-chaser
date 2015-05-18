#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

# -*- coding: utf-8 -*-


from django import apps
from django.db.models.signals import pre_save

from sensor.core.signals.handlers import (
    create_generic_sensor_for_sensor,
    create_generic_event_for_event, add_missing_sensor_type_to_sensor)


class AppConfig(apps.AppConfig):

    name = 'sensor.core'
    verbose_name = 'Sensor Core'

    def ready(self):

        pre_save.connect(add_missing_sensor_type_to_sensor)
        pre_save.connect(create_generic_sensor_for_sensor)
        pre_save.connect(create_generic_event_for_event)