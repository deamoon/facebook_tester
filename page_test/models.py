from django.db import models
from testyourface import settings

class Company(models.Model):
    level = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    token = models.CharField(max_length=250)
    id_page = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=300)
    start = models.DateTimeField()
    end = models.DateTimeField()
    number_photos = models.IntegerField(blank=True)
    current_photo_id = models.IntegerField(blank=True)
    likes = models.IntegerField(default=0)
    album_cover = models.CharField(max_length=30, default='')

    def __unicode__(self):
        return 'Company ' + self.name

class Images(models.Model):
	id_photo = models.CharField(max_length=50)
	company = models.ForeignKey(Company)
	number = models.IntegerField()
	likes = models.IntegerField(default=0)
	source = models.CharField(max_length=355)

class UserToken(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	token = models.CharField(max_length=250)
	id_facebook = models.CharField(max_length=50)