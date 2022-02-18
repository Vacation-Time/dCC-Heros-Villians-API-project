from django.db import models
from .models import *


# Create your models here.


class SuperType(models.Model):
    type = models.CharField(max_length=255)

    # def __str__(self) -> str:
    #     return super().__str__()
