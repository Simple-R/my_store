from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse

import logging
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout

import json
import datetime
import logging

from .forms import CreateUserForm
from django.contrib import messages

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



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
	data = json.loads(request.body)
	product_id = data["product_id"]
	action = data["action"]
	
	return JsonResponse("Item was updated")


def process_order(request):
	# Do Stuff here
	
	return JsonResponse("Order Processed")


def login_user(request):
	"""For logging in an authenticated  user"""

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			logging.debug(f"{username} is Logged in")###
			return redirect("market:market")
			
		else: messages.error(request, 'Account not Registered')

	
	return render(request, 'market/login.html')


def register_user(request):
	# Do Stuff here

	context = {}
	return render(request, 'market/register.html', context)
