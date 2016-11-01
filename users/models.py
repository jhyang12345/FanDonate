from django.db import models

from core.models import TimeStampedModel
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
# Create your models here.

class FanUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, first_name="", last_name="", gender="male"):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            gender = gender,
            date_of_birth = date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class FanUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)

    objects = FanUserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email
