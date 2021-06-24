from django.db import models

# Create your models here.

class Reserv(models.Model):
    stu_id = models.IntegerField()
    writer = models.CharField(max_length= 100)
    room = models.CharField(max_length = 100)
    res_time = models.DateTimeField()

    def __str__(self):
        return self.room

