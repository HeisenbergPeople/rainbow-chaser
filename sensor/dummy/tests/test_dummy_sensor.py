from unittest import TestCase
from sensor.dummy.models import DummySensor

__author__ = 'bradley'

class TestDummySensor(TestCase):

    def test_dummy_sensor_create(self):

        try:
            sensor = DummySensor()
        except:
            self.fail()

        self.assertTrue(True)
