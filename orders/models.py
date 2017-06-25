from django.db import models
#from django.contrib.auth import get_user_model

from Carts.models import Cart

# Create your models here.
# try:
#     from django.contrib.auth import get_user_model
#     User = get_user_model()
# except ImportError:
    

from django.contrib.auth.models import User  

STATUS_CHOICES = (
		('Started','Started'),
		('Processing','Processing'),
		('Abandoned','Abandoned'),
		('Finished','Finished'),
	)

class Order(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	# USER
	# address
	order_id = models.CharField(max_length=200, default="ABC", unique=True)
	cart = models.ForeignKey(Cart)
	status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="Started")

	sub_total = models.DecimalField(default=10.00, decimal_places=2, max_digits=1000)
	tax_total = models.DecimalField(default=10.00, decimal_places=2, max_digits=1000)
	final_total = models.DecimalField(default=10.00, decimal_places=2, max_digits=1000)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)


	def __unicode__(self):
		return str(self.order_id)
		