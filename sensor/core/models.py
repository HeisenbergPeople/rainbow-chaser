#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.db import models


class Sensor(models.Model):
    """A sensor measures one kind of thing. A physical device might have
    multiple logical sensors.
    """

    name = models.CharField(max_length=256)
    model = models.CharField(max_length=128)

    class Meta:
        unique_together = [('name', 'model')]