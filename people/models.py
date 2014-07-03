from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#user information 
#it contains accounts, mail, thirds-app, MessageBoard, Sharesite
#class People(models.Model):
#	username = models.CharField(max_length=20)
#	password = models.CharField(max_length=20)

#user's messageboard
class MessageBoard(models.Model):
	account = models.ForeignKey(User)
	user = models.CharField(max_length=20)
	pub_date = models.DateTimeField('date published')
	star = models.IntegerField()
	agree = models.IntegerField()
	content = models.CharField(max_length=500)

#user's mail
#class Mail(models.Model):
#	pass
