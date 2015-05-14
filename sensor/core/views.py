#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json

from django.http import HttpResponse, HttpRequest
from django.views.generic import View
from sensor.core.models import GenericSensor, Sensor


class DataUploadView(View):
    """A view for uploading measurements."""

    forms = {}

    @classmethod
    def register(cls, sensor_class):
        """DataUploadView.register(sensor_class)

        Registers a form and model class with the given sensor type name.
        This method should not be called once all the apps are loaded and
        running -- only during startup.
        """

        if not issubclass(sensor_class, Sensor):
            raise TypeError('{} is not a subclass of {}'.format(
                sensor_class, Sensor))

        cls.forms[sensor_class.sensor_type_name()] = \
            sensor_class.event_upload_form()

    def put(self, request, sensor_id):
        sensor_id = int(sensor_id)
        try:
            sensor = GenericSensor.objects.get(pk=sensor_id)
        except GenericSensor.DoesNotExist:
            return self.sensor_not_found(sensor_id)

        except GenericSensor.MultipleObjectsReturned:
            return self.internal_error()

        if not sensor.sensor_type.name in self.__class__.forms:
            return self.unknown_sensor_type()

        form_class = self.__class__.forms[sensor.sensor_type.name]

        try:
            data = json.loads(request.body)
        except ValueError:
            return self.malformed_data_response()

        form = form_class(data)

        if not form.is_valid():
            return self.invalid_data(form.errors)

        form.save()
        return JSONResponse({'status': 'ok'})

    def sensor_not_found(self, sensor_id):
        return JSONResponse({
            'status': 'unknown_sensor',
            'long_description':
                'There is no sensor with id {}'.format(sensor_id),
            },
            status=404)

    def internal_error(self):
        return JSONResponse({
            'status': 'internal_error',
            },
            status=500)

    def unknown_sensor_type(self):
        return JSONResponse({
            'status': 'unknown_sensor_type',
            'long_description':
                'The sensor type for this sensor was not registered ' +
                'with the data upload view.',
            },
            status=500)

    def malformed_data_response(self):
        return JSONResponse({
            'status': 'malformed_data',
            'long_description': 'The request body was not valid JSON.'
        },
        status=400)

    def invalid_data(self, form_errors):
        return JSONResponse({
            'status': 'validation_error',
            'long_description': 'Data validation has failed.',
            'details': form_errors,
        },
        status=400)


class JSONResponse(HttpResponse):
    def __init__(self, data, *args, **kwargs):
        super(JSONResponse, self).__init__(
            json.dumps(data), *args, content_type='text/json', **kwargs)