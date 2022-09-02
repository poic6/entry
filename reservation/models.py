from django.db import models
from django.utils import timezone
import datetime as dt

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=13)
    schoolName = models.CharField(max_length=20)
    gradeNumber = models.IntegerField()
    regDate = models.DateTimeField(default=timezone.now())
    useTicket = models.IntegerField(default="0")
    useDate = models.DateTimeField(default=dt.datetime.strptime("1900-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))

    def __str__(self):
        return self.name