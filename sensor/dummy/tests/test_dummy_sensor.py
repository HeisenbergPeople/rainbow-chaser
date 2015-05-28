from unittest import TestCase
from sensor.dummy.models import DummySensor

__author__ = 'bradley'


def create_if_not_exist_sensor_type(name):
    sensor_types = SensorType.objects.filter(name=name)
    if len(sensor_types) == 0:
        sensor_type = SensorType(name=name)
        sensor_type.save()
        return sensor_type
    return sensor_types[0]


class TestDummySensor(TestCase):

    def test_dummy_sensor_create(self):

        try:
            sensor = DummySensor()
        except:
            self.fail()

        self.assertTrue(True)
