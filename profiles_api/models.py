from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Manager for User profiles

    Arguments:
        BaseUserManager {[type]} -- [description]
    """

    def create_user(self, email, name, password=None):
        """
        Create new user

        Arguments:
            email {[type]} -- [description]
            name {[type]} -- [description]

        Keyword Arguments:
            password {[type]} -- [description] (default: {None})

        Raises:
            ValueError: [description]

        Returns:
            [type] -- [description]
        """
        if not email:
            raise ValueError('User must have a email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Create a superuser

        Arguments:
            email {[type]} -- [description]
            name {[type]} -- [description]
            password {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    DataBase Model for users in the system    
    Arguments:
        AbstractBaseUser {[type]} -- [description]
        PermissionsMixin {[type]} -- [description]
    """
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_for_name(self):
        """
        Retrieve full name of user
        """
        return self.name

    def get_short_name(self):
        """
        Retrieve short name of user
        """
        return self.name

    def __str__(self):
        return self.email
