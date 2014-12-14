import datetime

from django.views.generic import TemplateView
from django.views.generic.list import ListView

from models import Button, Event


class AddButtonEventView(TemplateView):

    template_name = "add_button_event.html"

    def get(self, request, *args, **kwargs):

        button_name = self.kwargs['name']
        event_state = self.kwargs['state']

        d = self.kwargs['datetime'].split('_')
        date = d[0].split('-')
        time = d[-1].split('-')

        event_datetime = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))

        # wyciagnij button  z bazy
        b, was_created = Button.objects.get_or_create(name=button_name)

        event = Event.objects.create(state=event_state, datetime=event_datetime, button=b)
        print event

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class ListEventsView(ListView):
    template_name = 'list_events.html'
    model = Event
