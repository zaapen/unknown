from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import bcrypt

class UserManager(models.Manager):
	def validate_reg(self, data):
		errors = []
		if len(data['name']) < 3:
			errors.append("Name field must have at least 3 characters")
		if len(data['username']) < 3:
			errors.append("username field must have at least 3 characters")
		if len(self.filter(username=data['username'])) > 0:
			error.append("Username already in use")
		if len(data['password']) < 8:
			errors.append("Password must be 8 characters or more")
		if data['confirm_pw'] != data['password']:
			errors.append("confirm password does not match")
		if not errors:
			hash_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt().encode())
			user = self.create(name=data['name'], username=data['username'], password=hash_pw)
			return user
		else:
			return errors

	def validate_login(self, data):
		errors = []
		if len(self.filter(username=data['username'])) > 0:
			user = self.filter(username=data['username'])[0]
			if not bcrypt.checkpw(data['password'].encode(), user.password.encode()):
				errors.append("Incorrect password")
		else:
			errors.append("Username not found")

		if errors:
			return errors
		return user

class TripManager(models.Manager):
	def validate_trip(self, data):
		errors = []
		time = datetime.now().strftime('%Y-%m-%d')
		if len(data['destination']) < 1:
			errors.append("Destination is empty")
		if len(data['desc']) < 1:
			errors.append("Description is empty")
		if len(data['travel_start']) < 1 or len(data['travel_end']) < 1:
			errors.append("Please pick a date")
		if data['travel_start'] <= time:
			errors.append("From Date cannot be today")
		if data['travel_end'] < data['travel_start']:
			errors.append("You need a DeLorean with a Flux capacitor (see Back to the Future)")
		return errors

	def add_trip(self, data):
		this_user = User.objects.get(id=request.session['user_id'])
		this_trip = Trip.objects.create(destination=data['destination'], desc=data['desc'], travel_start=data['travel_start'], travel_end=data['travel_end'])
		return this_user.add(this_trip)


class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Trip(models.Model):
	destination = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	travel_start = models.DateField()
	travel_end = models.DateField()
	joiners = models.ManyToManyField(User, related_name="trips")
	objects = TripManager()