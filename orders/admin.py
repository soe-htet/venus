from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
	class Meta:
		model = Order
admin.site.register(Order,OrderAdmin)