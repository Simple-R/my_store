from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Group


from .models import Customer
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -- %(message)s')


def create_profile(sender, instance, created, **kwargs):
	"""The signal for Creating a New User"""
	
	if created:
		group =  Group.objects.get(name='Customer') # Stopped Here
		instance.groups.add(group)
		Customer.objects.create(user=instance, customer_name=instance.username)
		logging.debug("Profile Created")

post_save.connect(create_profile, sender=User)


"""
def update_profile(sender, instance, created, **kwargs):

	if created == False:
		instance.customer.save()
		print("Profile Updated")

post_save.connect(update_profile, sender=User)"""