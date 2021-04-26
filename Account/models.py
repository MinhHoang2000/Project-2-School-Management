from Account.managers import AccountManager
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from django.utils import timezone
from .managers import AccountManager
from django.contrib.auth.models import _user_has_perm

# Create your models here.

class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    permission_name = models.CharField(max_length=250)
    permission_code = models.CharField(max_length=128)

    class Meta:
        db_table = "permission"


class Account(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=128,
                                unique=True,
                                validators=[UnicodeUsernameValidator()],
                                error_messages={'unique': 'Username already exists'},
                                )
    password = models.CharField(max_length=320)
    email = models.CharField('Email of Account',
                             max_length=128,
                             validators=[EmailValidator()]
                             )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    join_at = models.DateTimeField('Time join', default=timezone.now)
    permissions = models.ManyToManyField(Permission)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_staff:
            return True
        return _user_has_perm(self, perm, obj)

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_staff

    @property
    def is_superuser(self):
        return self.is_admin

    def __str__(self):
        return self.username

    class Meta:
        db_table = "account"