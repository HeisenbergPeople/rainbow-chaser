#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls import patterns, include, url

from django.contrib import admin
from sensor.core.views import DataUploadView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/sensor/(?P<sensor_id>[1-9][0-9]*)/events',
        DataUploadView.as_view(), name='data_upload'),
    url(r'^thermometer/', include('thermometer.urls')),
)
