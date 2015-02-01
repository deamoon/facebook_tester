from django.db import models

class Piano(models.Model):
    note = models.IntegerField()