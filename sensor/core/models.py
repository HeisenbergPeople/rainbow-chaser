#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.db import models


class SensorType(models.Model):
    """Represents a type of sensors."""

    name = models.CharField(max_length=128, unique=True)


class GenericSensor(models.Model):
    """Represents a sensor abstracting away the specifics of what it measures.

    A sensor measures one kind of thing. A physical device might have
    multiple logical sensors belonging to different sensor types.
    """

    name = models.CharField(max_length=256)
    sensor_type = models.ForeignKey('core.SensorType')

    class Meta:
        unique_together = [('name', 'sensor_type')]


class Sensor(models.Model):
    """Base class for specific sensor types."""

    generic_sensor = models.OneToOneField('core.GenericSensor')

    class Meta:
        abstract = True


class GenericEvent(models.Model):
    """Represents a measurement event abstracting away what exactly is
    measured.
    """

    sensor = models.ForeignKey('core.GenericSensor')
    datetime = models.DateTimeField()
    value = models.CharField(max_length=128)


class Event(models.Model):
    """Base class for sensor-specific event types"""

    generic_event = models.OneToOneField('core.GenericEvent')

    class Meta:
        abstract = True