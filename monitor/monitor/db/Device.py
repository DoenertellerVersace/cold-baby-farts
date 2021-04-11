from django.db import models


class Device(models.Model):

    device_name = models.CharField()
    device_id = models.CharField()
    next_test = models.CharField()
    room = models.CharField("todefine")

