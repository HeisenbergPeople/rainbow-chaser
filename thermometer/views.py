import datetime

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from models import Sensor, Thermometer, Event

class MainView(TemplateView):

    template_name = 'thermometer_index.html'

    def get_context_data(self, **kwargs):

        context = super(MainView, self).get_context_data(**kwargs)
        print context
        context['thermometers'] = Thermometer.objects.all()
        context['sensors'] = Sensor.objects.all()
        print context
        return context

    def get(self, request, *args, **kwargs):

       context = self.get_context_data(**kwargs)
       return self.render_to_response(context)

class ThermometerDetail(DetailView):

    template_name = 'thermometer_detail.html'
    model = Thermometer
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super(ThermometerDetail, self).get_context_data(**kwargs)
        context['desc_len'] = len(context['object'].description)
        return context

class SensorDetail(DetailView):

    template_name = 'sensor_detail.html'
    model = Sensor
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super(SensorDetail, self).get_context_data(**kwargs)
        print context
        return context

class AddEvent(TemplateView):

    template_name = 'add_event.html'

    def get(self, request, *args, **kwargs):

        thermometer_name = self.kwargs['name']
        event_temperature = self.kwargs['temperature']
        d = self.kwargs['datetime'].split('_')
        date = d[0].split('-')
        time = d[-1].split('-')

        event_datetime = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))
        try:
            event_thermometer = Thermometer.objects.get(name=thermometer_name)
            print event_thermometer

            event = Event.objects.create(temperature=event_temperature,
                                         datetime=event_datetime,
                                         thermometer=event_thermometer)

            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)

        except ObjectDoesNotExist:
            print 'Does not exist'
            return HttpResponse('<h1>Illegal thermometer name</h1>')

class ListEvents(ListView):
    template_name = 'list_thermo_events.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super(ListEvents, self).get_context_data(**kwargs)
        if 'name' in self.kwargs:
            name = self.kwargs['name']
            print name
            b = Thermometer.objects.all().filter(name=self.kwargs['name'])
            print b
            context['events'] = self.object_list.filter(thermometer=b)
        else:
            context['events'] = self.object_list

        context['thermometers'] = Thermometer.objects.all()

        return context
