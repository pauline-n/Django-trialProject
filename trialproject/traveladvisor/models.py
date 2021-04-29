from django.db import models

# Create your models here.
class BookaTrip(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=80)
    travel_date = models.DateTimeField()

    def __str__(self):
        return self.name