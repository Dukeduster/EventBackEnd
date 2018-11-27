from django.db import models

# Create your models here.

class UserApp(models.Model):
	id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	email=models.CharField(max_length=256)
	def __str__(self):
		return str(self.username)

class Event(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	owner=models.ForeignKey('UserApp', on_delete=models.CASCADE)
	creationDate=models.DateTimeField(auto_now_add=True)
	enabled=models.BooleanField(default=True)
	description=models.CharField(max_length=100, blank=True, null=True)
	expireDate=models.DateTimeField(blank=True,null=True)
	def __str__(self):
		return str(self.name)

class EventSession(models.Model):
	id=models.CharField(max_length=50, primary_key=True)
	dateSession=models.DateTimeField(null=False)
	name=models.CharField(max_length=50)
	event=models.ForeignKey('Event', on_delete=models.CASCADE)
	description=models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return str(self.name)

class Attendance(models.Model):
	id=models.AutoField(primary_key=True)
	attendanceDate=models.DateTimeField(null=False)
	reportDate=models.DateTimeField(auto_now_add=True)
	session=models.ForeignKey('EventSession', on_delete=models.CASCADE)
	attendant=models.ForeignKey('UserApp', on_delete=models.CASCADE)
	latitude=models.DecimalField(max_digits=9, decimal_places=6)
	longitude=models.DecimalField(max_digits=9, decimal_places=6)
	def __str__(self):
		return str(self.attendanceDate)
