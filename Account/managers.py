from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


class AccountManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):

        if not username:
            raise ValueError("Account must have username")

        username = AbstractBaseUser.normalize_username(username)
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **kwargs):
        user = self.create_user(username, password, **kwargs)
        user.is_admin = True
        if user.is_admin is not True:
            raise ValueError('Admin is_admin have to be True')
        user.save()
        return user