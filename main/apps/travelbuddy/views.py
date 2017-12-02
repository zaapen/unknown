from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
	return render(request, 'travelbuddy/index.html')

def register(request):
	result = User.objects.validate_reg(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/')
	else:
		print result.id
		request.session['user_id'] = result.id
		messages.error(request, "Register successful")
		return redirect('/success')

def success(request):
	context = {
		"user": User.objects.get(id=request.session['user_id'])
	}
	return render(request, 'travelbuddy/success.html', context)

def login(request):
	result = User.objects.validate_login(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/')
	else:
		request.session['user_id'] = result.id
		return redirect('/travels')

def logout(request):
	request.session.flush()
	return redirect ('/')

def travels(request):
	current_user = User.objects.get(id=request.session['user_id'])
	user_trips = current_user.trips.all()
	all_users = User.objects.all()
	all_trips = Trip.objects.all()
	print all_users
	print all_trips
	context = {
		"current_user": current_user,
		"all_users": all_users,
		"user_trips": user_trips,
		"all_trips": all_trips 
	}
	return render(request, 'travelbuddy/travels.html', context)

def add(request):
	return render(request, 'travelbuddy/addtrip.html')

def create_trip(request):
	current_user = User.objects.get(id=request.session['user_id'])
	result = Trip.objects.validate_trip(request.POST)
	if result:
		for error in result:
			messages.error(request, error)
		return redirect('/travels/add')
	else:
		this_trip = Trip.objects.create(destination=request.POST['destination'], desc=request.POST['desc'], travel_start=request.POST['travel_start'], travel_end=request.POST['travel_end'])
		this_trip.joiners.add(current_user)
		return redirect('/travels')

def join(request, trip_id):
	current_user = User.objects.get(id=request.session['user_id'])
	current_trip = Trip.objects.get(id=trip_id)
	current_trip.joiners.add(current_user)
	return redirect('/travels')

def show(request, trip_id):
	current_trip = Trip.objects.get(id=trip_id)
	all_users = current_trip.joiners.all()
	first_user = current_trip.joiners.all()[0]
	context = {
		"current_trip": current_trip,
		"all_users": all_users,
		"first_user": first_user
	}
	return render(request, 'travelbuddy/showtrip.html', context)


