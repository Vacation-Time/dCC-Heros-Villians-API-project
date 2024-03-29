from django.db import models
from asyncore import write
from dataclasses import fields
from rest_framework import serializers
from .models import SuperType


class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'type']
        depth = 1
