from django.db import models
from django.contrib.auth.models import User


class Instrument(models.Model):
    name = models.CharField(max_length = 255)
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    def __str__(self):
        return self.name + " " + str(self.user)


class Sensor(models.Model):
    name = models.CharField(max_length = 255)
    instrument = models.ForeignKey(
        Instrument,
        on_delete = models.CASCADE
    )
    def __str__(self):
        return self.name + " " + str(self.instrument)


class TimeSeriesDatum(models.Model):
    value = models.FloatField()
    time = models.DateField(auto_now_add = True)
    sensor = models.ForeignKey(
        Sensor,
        on_delete = models.CASCADE
    )
    def __str__(self):
        return str(self.sensor) +''+ str(self.value)
