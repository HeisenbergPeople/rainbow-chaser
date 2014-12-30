# -*- coding: utf-8 -*-
from django.db import models

class Sensor(models.Model):

    name = models.CharField(max_length=20)
    min_temperature = models.IntegerField()
    max_temperature = models.IntegerField()
    accuracy = models.FloatField()

    def __unicode__(self):

        return 'Sensor %s\t Range[%s, %s]\taccuracy: %s' % (self.name, self.min_temperature,
                                                          self.max_temperature, self.accuracy)

class Thermometer(models.Model):

    name = models.CharField(max_length=100, unique=True)
    sensor = models.ForeignKey(Sensor, related_name='thermometer')
    description = models.CharField(max_length=200, blank=True)

    def __unicode__(self):

        return 'Thermometer: %s\t%s' % (self.name, self.sensor)

class Event(models.Model):

    datetime = models.DateTimeField()
    thermometer = models.ForeignKey(Thermometer, related_name='events')
    temperature = models.FloatField()

    def __unicode__(self):

        return 'Thermometer: %s\ttemperature: %s\tDatetime: %s' % (
            self.thermometer, self.temperature, self.datetime)

    class Meta:
        unique_together = (('thermometer', 'datetime'),)
        ordering = ['-datetime']
