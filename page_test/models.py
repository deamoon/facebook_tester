from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model as user_model
User = user_model()

class Company(models.Model):
    level = models.IntegerField()
    user = models.ForeignKey(User)
    token = models.CharField(max_length=250)
    id_page = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=300)
    start = models.DateTimeField()
    end = models.DateTimeField()
    number_photos = models.IntegerField(blank=True)
    current_photo_id = models.IntegerField(blank=True)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return 'Company ' + self.name

class Images(models.Model):
	id_photo = models.CharField(max_length=50)
	company = models.ForeignKey(Company)
	number = models.IntegerField()
	likes = models.IntegerField(default=0)
	source = models.CharField(max_length=355)

class UserToken(models.Model):
	user = models.ForeignKey(User)
	token = models.CharField(max_length=250)
	id_facebook = models.CharField(max_length=50)