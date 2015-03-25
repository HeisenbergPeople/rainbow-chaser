#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.contrib import admin
from thermometer.models import Sensor, Thermometer, Event

class SensorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sensor, SensorAdmin)

class ThermometerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Thermometer, ThermometerAdmin)

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
