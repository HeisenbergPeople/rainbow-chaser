#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.db import models


VALUE_MAX_LEN = 128


class GenericEvent(models.Model):
    """Represents a measurement event abstracting away what exactly is
    measured.
    """

    sensor = models.ForeignKey('core.GenericSensor')
    datetime = models.DateTimeField()
    value = models.CharField(max_length=VALUE_MAX_LEN)


class Event(models.Model):
    """Base class for sensor-specific event types"""

    generic_event = models.OneToOneField('core.GenericEvent')

    sensor = models.ForeignKey('core.Sensor')
    datetime = models.DateTimeField()


    def value_to_string(self):
        """Event.value_to_string() -> unicode

        Returns a string representation of the
        """

        raise NotImplementedError(self.__class__.value_to_string)

    class Meta:
        abstract = True