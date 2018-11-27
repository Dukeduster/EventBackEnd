from rest_framework import serializers
from .models import UserApp
from .models import Event
from .models import EventSession
from .models import Attendance

class UserAppSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserApp
        fields=('id','username','password','name', 'lastname', 'email')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=('id','name','owner','creationDate', 'enabled', 'description', 'expireDate')

class EventSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventSession
        fields=('id','dateSession','name','description', 'event')

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=('id','attendanceDate','reportDate','session', 'attendant', 'latitude', 'longitude')

class AttendanceShowSerializer(serializers.ModelSerializer):
    attendant=UserAppSerializer()
    class Meta:
        model=Attendance
        fields=('id','attendanceDate','reportDate','session', 'attendant', 'latitude', 'longitude')
