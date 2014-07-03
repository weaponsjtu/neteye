from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	def __unicode__(self):
		return self.choice
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()

class Onesite(models.Model):
	user = models.ForeignKey(User)
	tags = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	logo = models.CharField(max_length=100)
	domain = models.CharField(max_length=50)
	value = models.CharField(max_length=50)
	info = models.CharField(max_length=500)
	skill = models.CharField(max_length=500)
	shareusers = models.CharField(max_length=1000)
	pub_date = models.DateTimeField('date published')

class Comments(models.Model):
	onesite = models.ForeignKey(Onesite)
	user = models.CharField(max_length=20)
	pub_date = models.DateTimeField('date published')
	star = models.IntegerField()
	agree = models.IntegerField()
	content = models.CharField(max_length=500)
