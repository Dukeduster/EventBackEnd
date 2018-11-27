from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import UserApp, Event, EventSession, Attendance
from .serializers import UserAppSerializer, EventSerializer, EventSessionSerializer, AttendanceSerializer, AttendanceShowSerializer

# Create your views here.
class UserAppView(generics.ListAPIView):
    serializer_class = UserAppSerializer
    def get_queryset(self):
        queryset = UserApp.objects.all()
        user = self.request.query_params.get('user', None)
        passw=self.request.query_params.get('passw', None)
        if user is not None:
            queryset = queryset.filter(username=user)
            queryset = queryset.filter(password=passw)
        return queryset

    def post(self, request):
        serializer = UserAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)


class EventView(generics.ListAPIView):
    serializer_class = EventSerializer
    def get_queryset(self):
            queryset = Event.objects.all()
            owner = self.request.query_params.get('owner', None)
            if owner is not None:
                queryset = queryset.filter(owner=owner)
            return queryset


    def post(self, request):
        serializer=EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

class EventSessionView(generics.ListAPIView):
    serializer_class = EventSessionSerializer
    def get_queryset(self):
            queryset = EventSession.objects.all()
            event = self.request.query_params.get('event', None)
            if event is not None:
                queryset = queryset.filter(event=event)
            return queryset

    def post(self, request):
        serializer=EventSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

class AttendanceView(APIView):
    def post(self, request):
        serializer=AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

class AttendanceViewByUser(generics.ListAPIView):
    serializer_class = AttendanceShowSerializer
    def get_queryset(self):
            queryset = Attendance.objects.all()
            user = self.request.query_params.get('usr', None)
            if user is not None:
                queryset = queryset.filter(attendant=user).select_related("attendant")
            return queryset


class AttendanceViewBySession(generics.ListAPIView):
    serializer_class = AttendanceShowSerializer
    def get_queryset(self):
            queryset = Attendance.objects.all()
            session = self.request.query_params.get('session', None)
            if session is not None:
                queryset = queryset.filter(session=session)
            return queryset
