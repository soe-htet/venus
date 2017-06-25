from django.shortcuts import render, HttpResponseRedirect

from django.core.urlresolvers import reverse

# Create your views here.
from products.models import Product, Variation
from .models import Cart, CartItem

def view(request):
	try:
		the_id = request.session['cart_id']
	except:
		the_id = None
	if the_id:
		cart = Cart.objects.get(id=the_id)
		new_price = 0.00
		for item in cart.cartitem_set.all():
			line_total = float(item.product.price) * item.quantity
			new_price += line_total

		request.session['items_total'] = cart.cartitem_set.count()
		cart.total = new_price
		cart.save()
		context = {"cart":cart}
	else:
		message = "Your Cart is Empty! please Keep Shopping"
		context = {"empty":True, "message":message}
	return render(request, 'carts/view.html',context)


def remove_cart(request, id):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		return HttpResponseRedirect(reverse('cart'))

	cart_item = CartItem.objects.get(id=id)
	cart_item.cart = None
	cart_item.save()

	return HttpResponseRedirect(reverse('cart'))

def update_cart(request, slug):
	qty = None
	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id

	cart = Cart.objects.get(id=the_id)
	try:
		product = Product.objects.get(slug=slug)
	except product.DoesNotExist:
		raise
	except:
		pass


	product_var = []
	if request.method == "POST":
		qty = request.POST['qty']
		for item in request.POST:
			key = item
			val = request.POST[key]

			try:
				v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
				product_var.append(v)
			except:
				pass


		cart_item = CartItem.objects.create(cart=cart, product=product)
		
		if int(qty)==0:
				cart_item.delete()
			
		if len(product_var) > 0:
			cart_item.variations.clear()
			cart_item.variations.add(*product_var)
		cart_item.quantity = qty
		cart_item.save()
				

		# if not cart_item in car.products.all():
		# 	cart.products.add(product)
		# else:
		# 	cart.products.remove(product)

		new_price = 0.00
		for item in cart.cartitem_set.all():
			line_total = float(item.product.price) * item.quantity
			new_price += line_total

		request.session['items_total'] = cart.cartitem_set.count()
		cart.total = new_price
		cart.save()

	return HttpResponseRedirect(reverse('cart'))