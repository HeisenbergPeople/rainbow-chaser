#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.db import models


class GenericSensor(models.Model):
    """Represents a sensor abstracting away the specifics of what it measures.

    A sensor measures one kind of thing. A physical device might have
    multiple logical sensors.
    """

    name = models.CharField(max_length=256)
    model = models.CharField(max_length=128)

    class Meta:
        unique_together = [('name', 'model')]


class Sensor(models.Model):
    """Base class for specific sensor types."""

    generic_sensor = models.OneToOneField(GenericSensor)

    class Meta:
        abstract = True


class GenericEvent(models.Model):
    """Represents a measurement event abstracting away what exactly is
    measured.
    """

    sensor = models.ForeignKey(GenericSensor)
    datetime = models.DateTimeField()
    value = models.CharField(max_length=128)