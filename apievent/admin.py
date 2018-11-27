from django.contrib import admin
from .models import UserApp, Event, EventSession, Attendance

# Register your models here.
admin.site.register(UserApp)
admin.site.register(Event)
admin.site.register(EventSession)
admin.site.register(Attendance)


