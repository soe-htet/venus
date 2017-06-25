from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=200, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2,max_digits=100, default=00.00)
	sale_price = models.DecimalField(decimal_places=2,max_digits=100, default=00.00, null=True,blank=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return str(self.title)

	class Meta:
		unique_together = ('title','slug')
			

	def get_price(self):
		return self.price

	def get_absolute_url(self):
		return reverse("single_product", kwargs={"slug":self.slug})


class  ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='products/image/')
	title = models.CharField(max_length=120,null=True,blank=True)
	feature_image = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)


	def __unicode__(self):
		return str(self.title)



class Tag(models.Model):
	product = models.ForeignKey(Product)
	tag = models.CharField(max_length=20)
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return str(self.tag)


class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager,self).filter(active=True)

	def sizes(self):
		return self.all().filter(category='size')

	def colors(self):
		return self.all().filter(category='color')

		

VAR_CATEGORIES = (
		('color','color'),
		('size','size'),
		('package','package')
	)

class Variation(models.Model):
	product = models.ForeignKey(Product)
	category = models.CharField(max_length=120,choices=VAR_CATEGORIES, default='color')
	title = models.CharField(max_length=120,null=True,blank=True)
	image = models.ForeignKey(ProductImage, null=True, blank=True)
	price = models.DecimalField(decimal_places=2,max_digits=100, default=00.00)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	active = models.BooleanField(default=True)

	objects = VariationManager()

	def __unicode__(self):
		return str(self.title)
			