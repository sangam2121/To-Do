from django.db import models
from django.utils import timezone
# Create your models here.

class myModel(models.Model):

    text = models.CharField(max_length=100)
    added_date = models.DateTimeField(default= timezone.now())
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)



    def __str__(self):
        return self.text