from django.shortcuts import render
import requests
import json
import os
from django.contrib.auth.models import User
from sampleapp.models import UserPlace,ActivityPeriods
from datetime import datetime
from django.http.response import JsonResponse
from rest_framework import viewsets, generics,views
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserlistSerializer,ActivityPeriodlistSerializer,UserPlaceSerializer
from django.forms.models import model_to_dict


# save users

def home(request):

    with open("useractivity.json", "r") as config:
        jsonData = json.load(config)
        ActivityPeriods.objects.all().delete()
        UserPlace.objects.all().delete()
        User.objects.all().delete()
        for data in jsonData['members']:
            users = User.objects.create(username=data['real_name'])
            place = UserPlace.objects.create(user_id=users.id,place=data['tz'])
            for  active  in data['activity_periods']:
                start = datetime.strptime(active['start_time'], '%b %d %Y %I:%M%p')
                end = datetime.strptime(active['end_time'], '%b %d %Y %I:%M%p')
                activity = ActivityPeriods.objects.create(user_id=users.id,start_time=start,end_time=end)
                
        return JsonResponse({'success':True, 'data':jsonData})

# list user details

class UserViewSet(views.APIView):

    def get(self, request):
         results = []
         for item in User.objects.all():
             activity_periods = ActivityPeriods.objects.filter(user_id=item.id).values('start_time','end_time')
             user_place = UserPlace.objects.filter(user_id=item.id).values('place')
             results.append({
                 'real_name':item.username,
                 'id':item.id,
                 'activity_periods':list(activity_periods),
                 'tz':list(user_place),
                 
             })
         return Response({'ok':True, 'members':results})
        
