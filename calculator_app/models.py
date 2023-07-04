from django.db import models

# Create your models here.

class Computation(models.Model):
    first_number = models.CharField(max_length=250)
    operation = models.CharField(max_length=250)
    second_number = models.CharField(max_length=250)
    answer = models.CharField(max_length=255)
    #result = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return self.first_number + " " + self.operation + " " + self.second_number
    