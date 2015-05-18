from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Hobby(models.Model):
	name = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
	user = models.ForeignKey(User)

	birthdate = models.DateField(blank=True)

	HAIR_COLOR_CHOICES = (
		('BLACK', 'Black'),
		('BROWN', 'Brown'),
		('RED', 'Red'),
		('BLONDE', 'Blonde'),
		('SALTNPEPPER', 'Salt N Peppa'),
		('GREEN', 'Green'),
		('BALD', 'Fucking Bald'),
	)

	hair_color = models.CharField(max_length=128,
		choices = HAIR_COLOR_CHOICES,
		blank = True)

	favorite_hobby = models.ForeignKey(Hobby)

	created = models.DateTimeField(default=datetime.now())

	def __unicode__(self):
		return self.user.username
