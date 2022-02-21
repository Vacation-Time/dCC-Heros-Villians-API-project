from django.db import models
from asyncore import write
from dataclasses import fields
from rest_framework import serializers
from .models import Supers


class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id', 'name', 'alter_ego', 'primary_ability',
                  'secondary_ability', 'catchphrase', 'super_type']
        depth = 1
    # super_type_id = serializers.IntegerField(write_only=True) # this line prevents api from working-why?
