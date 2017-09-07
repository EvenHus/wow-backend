from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Help Django work with our custom user model."""

    def create_user(self, email, name, password):
        """Create a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a "user profile " inside our system."""

    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        """Used to get a users short name."""

        return self.name

    def __str__(self):
        """Django uses this when is need to convert the object to a string"""

        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update."""

    user_profile_image = models.ImageField(null=True)
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=225)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the model as a string."""

        return self.status_text


class ProfileFeedImage(models.Model):
    """Add image to feed."""

    image = models.ImageField(null=True)
    image_text = models.CharField(max_length=225)
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the model as a string"""

        return self.image_text
