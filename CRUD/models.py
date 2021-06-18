from django.db import models

a = {}
# Create your models here.
class Task(models.Model):

    task     = models.CharField(blank=False, max_length=200, )
    complete = models.BooleanField(default=True, blank=False, null=False)
    date     = models.DateField(auto_now_add=True)
    time     = models.TimeField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.task 

