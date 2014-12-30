from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.MainView.as_view(), name='thermometer_index'),
                       url(r'^(?P<name>[A-Za-z_][A-Za-z0-9_]*)$', views.ThermometerDetail.as_view(), name='thermometer_detail'),
                       url(r'^sensor/(?P<name>.*)$', views.SensorDetail.as_view(), name='sensor_detail'),
                       url(r'^add/(?P<name>.*)/(?P<temperature>.*)/(?P<datetime>.*)$', views.AddEvent.as_view(), name='add_temperature_event'),
                       url(r'^list/$', views.ListEvents.as_view(), name='thermometer_list'),
                       url(r'^list/(?P<name>.*)/$', views.ListEvents.as_view(), name='thermometer_list'),

)
