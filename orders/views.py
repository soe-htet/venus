import time
from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

from Carts.models import Cart
from .models import Order

from django.contrib import messages

from .utils import id_generator


from django.conf import settings

import sendgrid
import os
from sendgrid.helpers.mail import *



def user_orders(request):

	orders = Order.objects.filter(user=request.user)
	if orders:
		context = {'orders': orders}
	else:
		message = "You don't have any order"
		context = {"empty":True, "message":message}

	
	template = 'orders/user_orders.html'
	return render(request,template,context)

@login_required
def checkout(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
		print "no item id"
		return HttpResponseRedirect(reverse('cart'))

	new_order = Order()
	new_order.cart = cart
	new_order.user = request.user
	new_order.order_id = id_generator()
	new_order.save()


	context = {
			"order":new_order,
		}
	message = render_to_string("orders/order.txt", context)
	subject = "Order Detail"
	send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [request.user.email])


	try:
		sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(settings.SEND_GRID_API))
		from_email = Email("venusleague@gmail.com")
		to_email = Email(request.user.email)
		subject = "Orders Detail: " + new_order.order_id
		context = {
			"order":new_order,
		}
		message = render_to_string("accounts/activation_message.txt", context)
		content = Content("text/plain", message)
		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body=mail.get())
	except:
		pass


			
 	del request.session['cart_id']
	del request.session['items_total']

	new_cart = Cart()
	new_cart.save()
	request.session['cart_id'] = new_cart.id
	request.session['items_total'] = new_cart.cartitem_set.count()

	messages.warning(request, "Order placed. We have sent order details via email.")
	context = {'order':new_order}
	template = 'orders/order_details.html'
	return render(request,template,context)

	
	# ## run credig card
	# if new_order.status == "Finished":
	# 	cart.delete()
	# 	del request.session['cart_id']
	# 	del request.session['items_total']
	# 	return HttpResponseRedirect(reverse('cart'))


	# context = {}
	# template = 'products/home.html'
	# return render(request,template,context)