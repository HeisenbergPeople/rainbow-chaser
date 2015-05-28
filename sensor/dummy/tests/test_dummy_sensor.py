from unittest import TestCase
from sensor.core.models import SensorType, GenericSensor
from sensor.dummy.models.dummy_sensor import DummySensor

__author__ = 'bradley'


def create_if_not_exist_sensor_type(name):
    sensor_types = SensorType.objects.filter(name=name)
    if len(sensor_types) == 0:
        sensor_type = SensorType(name=name)
        sensor_type.save()
        return sensor_type
    return sensor_types[0]


def create_if_not_exist_generic_sensor(name, sensor_type):
    generic_sensors = GenericSensor.objects.filter(name=name, sensor_type=sensor_type)
    if len(generic_sensors) == 0:
        generic_sensor = GenericSensor(name=name, sensor_type=sensor_type)
        generic_sensor.save()
        return generic_sensor
    return generic_sensors[0]

class TestDummySensor(TestCase):

    def test_dummy_sensor_create(self):

        try:
            sensor = DummySensor()
        except:
            self.fail("Fail create object DummySensor")
        try:
            type_name = 'TestType'
            sensor_type = create_if_not_exist_sensor_type(type_name)
            sensor.generic_sensor = create_if_not_exist_generic_sensor(type_name, sensor_type)
            sensor.name = 'Test'
            sensor.sensor_type = sensor_type
        except:
            self.fail("Problem while assign value to attributes")
        try:
            sensor.save()
        except Exception, e:
            self.fail("Can't save to database %s" % str(e))
