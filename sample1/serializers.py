from rest_framework import serializers
from sampleapp.models import UserPlace,ActivityPeriods
from django.contrib.auth.models import User


class UserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ActivityPeriodlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = ('id', 'start_time','end_time','user_id')


class UserPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = UserPlace
        fields = ('id', 'place','user_id')