from django.db import models

# Create your models here.
class Line(models.Model):
    raw = models.TextField()
    timestamp = models.DateTimeField()
    cdata = models.TextField()