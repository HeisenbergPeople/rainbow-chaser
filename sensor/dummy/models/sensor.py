#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.


from sensor.core.models import Sensor


class DummySensor(Sensor):

    @classmethod
    def sensor_type_name(self):
        return "dummy_sensor"