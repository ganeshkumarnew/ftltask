from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from django.contrib.auth.models import User
from sampleapp.models import UserPlace,ActivityPeriods
from datetime import datetime


# save user

@api_view(["GET"])
def create_apicall(heightdata):
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

# list user

@api_view(["GET"])
def show_apicall(heightdata):
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