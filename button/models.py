from django.db import models

# Create your models here.
class Button(models.Model):

    # unique oznacza ze ta sma nazwa nie bedzie zarejestrowana dwa razy
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

class Event(models.Model):

    state_choices = ((True, 'Down'),
                     (False, 'Up'))

    state = models.CharField(max_length = 2,
                             choices=state_choices,
                             default=False)
    datetime = models.DateTimeField()
    button = models.ForeignKey(Button)

    def __unicode__(self):

        return "State: %s\tDateTime: %s\tButton: %s" % (self.state, self.datetime, self.button)

    class Meta:
        unique_together = (('button', 'datetime'),)
