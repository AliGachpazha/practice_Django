from django.contrib.auth.models import AbstractUser
from django.db import models
from . import config


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(verbose_name='نام',max_length=30)
    last_name = models.CharField(verbose_name='نام خانوادگی',max_length=30)
    age = models.IntegerField(null=True,verbose_name='سن')
    gender_type = models.CharField(verbose_name='جنسیت',max_length=600, choices=config.gender_type, null=False,
                                   blank=False)
    date_joined = models.DateTimeField(verbose_name='تاریخ پیوست', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='آخرین ورود', auto_now=True)
    phone = models.CharField(verbose_name='موبایل',validators=[config.phone_regex], max_length=10, unique=True)
    username = models.CharField(verbose_name='نام کاربری',max_length=60, unique=True)
    email = models.EmailField(verbose_name='ایمیل',max_length=60, unique=True)
