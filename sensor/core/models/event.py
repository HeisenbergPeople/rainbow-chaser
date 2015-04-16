#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.db import models


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