from django.db import models

# Create your models here.

class Myapp(models.Model):
  name = models.CharField(max_length=50, blank=False, default='')
  asal = models.CharField(max_length=50, blank=False, default='')

  class Meta:
    ordering =('id',)