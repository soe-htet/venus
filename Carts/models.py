from django.db import models

from products.models import Product, Variation

# Create your models here.

class Cart(models.Model):
	products = models.ManyToManyField(Product, null=True, blank=True)
	total = models.DecimalField(max_digits=200, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	active = models.BooleanField(default=True)


	def __unicode__(self):
		return "Card Id: %s" %(self.id)


class CartItem(models.Model):
	cart = models.ForeignKey(Cart, null=True, blank=True)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(decimal_places=2)
	variations = models.ManyToManyField(Variation, null=True,blank=True)
	notes = models.TextField(null=True, blank=True, default='')
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
		
	def __unicode__(self):
		return self.product.title