from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=13)
    schoolName = models.CharField(max_length=20)
    gradeNumber = models.IntegerField()
    regDate = models.DateTimeField()
    