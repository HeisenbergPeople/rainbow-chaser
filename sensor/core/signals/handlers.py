#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.db.models.signals import pre_save
from django.dispatch import receiver

from sensor.core.models import GenericSensor, Sensor, Event, GenericEvent, \
    SensorType


def add_missing_sensor_type_to_sensor(**kwargs):
    model_instance = kwargs['instance']

    if isinstance(model_instance, Sensor):
        sensor_type_name = model_instance.__class__.sensor_type_name()
        model_instance.sensor_type, __ = SensorType.objects.get_or_create(
            name=sensor_type_name)


def create_generic_sensor_for_sensor(**kwargs):
    model_instance = kwargs['instance']

    if isinstance(model_instance, Sensor):
        sensor = model_instance
        sensor.generic_sensor = GenericSensor.objects.create(
            name=sensor.name, sensor_type=sensor.sensor_type)


def create_generic_event_for_event(**kwargs):
    model_instance = kwargs['instance']

    if isinstance(model_instance, Event):
        event = model_instance
        event.generic_event = GenericEvent.create(
            sensor=event.sensor,
            datetime=event.datetime,
            value=event.value_to_string())