from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, PermissionsMixin
)
from django.db.models.fields import PositiveIntegerField
# Create your models here.

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    picture = models.FileField(null=True, upload_to='picture/')

    USERNAME_FIELD = 'email' #クラスを一意に識別
    REQUIRED_FIELDS = ['username'] #スーパーユーザを作る際に必要

    class Meta:
        db_table = 'users'
        