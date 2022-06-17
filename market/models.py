from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	"""Every registered User"""

	class Meta: verbose_name_plural = "Customers"
	
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	customer_name = models.CharField(max_length=200, null=True)
	customer_email = models.EmailField()



class Product(models.Model):
	""" The Product(s) in the market"""

	class Meta: verbose_name_plural = "Products"

	LABEL = (
		("digital","digital",),
		("non-digital","non-digital",)
		)
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=7, null=True, decimal_places=2)
	image = models.ImageField(null=True, blank=True)
	label = models.CharField(max_length=200, null=True, choices=LABEL)

	
	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		"""For Getting the image and diplaying nicely"""

		try:
			url = self.image.url

		except:
			url = ''

		return url


class Order(models.Model):
	"""Available Orders, completed or not"""

	class Meta:
		verbose_name_plural = "Orders"

	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_items(self):
		order_items = self.orderitem_set.all()
		total = sum([item.quantity for item in order_items])

		return total

	@property
	def get_cart_total(self):
		order_items = self.orderitem_set.all()
		total = sum([item.get_total for item in order_items])
		return total


class OrderItem(models.Model):
	"""Specific Orderitems"""
	class Meta:
		verbose_name_plural = "Order Items"

	product = models.ForeignKey(
		Product, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(
		Order, on_delete=models.SET_NULL, null=True, blank=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
