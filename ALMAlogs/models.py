from django.db import models

# Create your models here.
class Line(models.Model):
    raw = models.TextField()
    timestamp = models.DateTimeField()
    cdata = models.TextField()
    sourceobject = models.CharField(max_length=512)
    execblock = models.ForeignKey('ExecBlock', null=True)
    routine = models.TextField()
    type = models.TextField()

class ExecBlock(models.Model):
    uid = models.TextField()