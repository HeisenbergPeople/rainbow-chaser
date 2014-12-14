from django.contrib import admin
from iSensor.push_button.models import Button, Event

class ButtonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Button, ButtonAdmin)

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)


# Register your models here.
