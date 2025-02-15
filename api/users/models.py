from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from django.utils.translation import gettext_lazy as _

from api.users.managers import CustomUserManager
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email