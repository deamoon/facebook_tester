from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    level = models.IntegerField()
    user = models.ForeignKey(User)
    token = models.CharField(max_length=250)
    id_page = models.CharField(max_length=30)
    name = models.CharField(max_length=300)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return 'Company ' + self.name

class Images(models.Model):
	id_photo = models.CharField(max_length=50)
	company = models.ForeignKey(Company)
	number = models.IntegerField()