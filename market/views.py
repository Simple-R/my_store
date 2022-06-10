from django.shortcuts import render
from .models import *
from django.http import JsonResponse

import json
import datetime



def market(request):
	all_products = Product.objects.all()

	context = {
	    "products": all_products,
	}

	return render(request, 'market/index.html', context)


def cart(request):
	# Do Stuff here
	
	context = {}
	return render(request, 'market/cart.html', context)


def checkout(request):
	# Do Stuff here
	
	context = {}
	return render(request, 'market/checkout.html', context)


def update_item(request):
	# Do Stuff here
	
	return JsonResponse("Item was updated")


def process_order(request):
	# Do Stuff here
	
	return JsonResponse("Order Processed")