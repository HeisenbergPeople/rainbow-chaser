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
        """
        if not issubclass(sensor_class, Sensor):
            raise TypeError('{} is not a subclass of {}'.format(
                sensor_class, Sensor))

        cls.forms[sensor_class.sensor_type_name()] = \
            sensor_class.event_upload_form()

    def put(self, request, sensor_id):
        sensor_id = int(sensor_id)
        sensor = GenericSensor.objects.get(pk=sensor_id)
        form_class = self.__class__.forms[sensor.sensor_type.name]

        data = json.loads(request.body)
        form = form_class(data)

        if not form.is_valid():
            return HttpResponse(form.errors.as_json(), status=200)

        form.save()
        return HttpResponse(json.dumps({'status': 'ok'}))