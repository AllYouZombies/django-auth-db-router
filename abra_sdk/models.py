from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    use_in_migrations = True


class User(AbstractBaseUser):
    """ User class model used for authentication"""
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)

    objects = UserManager()

    class Meta:
        managed = False
        db_table = "auth_user"

    USERNAME_FIELD = 'username'
