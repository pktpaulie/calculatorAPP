from django.db import models

# Create your models here.

class Computation(models.Model):
    first_number = models.CharField(max_length=250, null=False)
    operation = models.CharField(max_length=250, null=False)
    second_number = models.CharField(max_length=250, null=False)
    answer = models.CharField(max_length=255, null=True, blank=False)
    #result = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return self.first_number + " " + self.operation + " " + self.second_number
    