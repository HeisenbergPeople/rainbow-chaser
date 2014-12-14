from django.db import models

# Create your models here.

class Button(models.Model):

    name = models.CharField(max_length=100)

class Event(models.Model):

    state_choices = ((True, 'Down'),
                     (False, 'Up'))

    state = models.CharField(max_length = 2,
                             choices=state_choices,
                             default=False)
    datetime = models.DateTimeField()
    button = models.ForeignKey(Button)
