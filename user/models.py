from django.db import models
from . import config
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender_type = models.CharField(max_length=600,choices=config.gender_type, null=False, blank=False)
    phone = models.CharField(validators=[config.phone_regex], max_length=10, unique=True)
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=30)