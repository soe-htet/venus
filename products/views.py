from django.shortcuts import render, Http404
from .models import Product

from marketing.models import Slider

# Create your views here.

def search(request):
	try:
		q = request.GET.get('q')
	except: 
		q= None

	if q:
		products = Product.objects.filter(title__icontains=q)
		context ={"query": q,"products": products}
	else:
		context ={"query": q,"products": Product.objects.all()}
	return render(request, "products/all.html",context)

def home(request):
	context ={"hello": "hello"}
	return render(request, "products/home.html",context)


def all(request):
	context ={
				"products": Product.objects.all(),
				"sliders": Slider.objects.all_featured(),
				}
	return render(request, "products/all.html",context)

def single(request,slug):
	try:
		product = Product.objects.get(slug=slug)
		print product.price
		context = {'product': product}
		return render(request, "products/single.html",context)
	except:
	 	raise Http404