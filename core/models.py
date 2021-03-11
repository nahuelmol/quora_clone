from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class Users(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=30)

@receiver(pre_save,sender=Users)
def pre_save_sign(sender,**kwargs):
	print('pre_save singal')

@receiver(post_save,sender=Users)
def post_save_sign(sender,**kwargs):
	print('post_save signal')


