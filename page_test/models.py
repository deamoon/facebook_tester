from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=250)
    id_page = models.CharField(max_length=30)
    name = models.CharField(max_length=300)

    def __unicode__(self):
       return 'Company ' + self.name