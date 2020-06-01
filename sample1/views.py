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




