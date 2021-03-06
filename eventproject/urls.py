"""assistproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apievent import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^events/$', views.EventView.as_view()),
    url(r'^sessions/$', views.EventSessionView.as_view()),
    url(r'^attendance/$', views.AttendanceView.as_view()),
    url(r'^users$', views.UserAppView.as_view()),
    url(r'^getAttendanceByUser$', views.AttendanceViewByUser.as_view()),
    url(r'^getAttendanceBySession$', views.AttendanceViewBySession.as_view())

]
