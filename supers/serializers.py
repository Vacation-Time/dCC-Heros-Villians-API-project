from django.db import models
from asyncore import write
from rest_framework import serializers
from .models import Supers


class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['name', 'alter_ego', 'primary_ability',
                  'secondary_ability', 'catchphrase', 'super_type_id']
    super_type_id = serializers.IntegerField(write_only=True)
