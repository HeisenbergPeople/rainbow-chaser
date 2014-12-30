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
