from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from django.utils.translation import gettext_lazy as _

from api.users.managers import CustomUserManager
from core.libs.models import TimeStampModel
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
    
class RequestLog(TimeStampModel):
    endpoint = models.CharField(
        max_length=1000, null=True
    )  # The url the user requested
    user = models.CharField(max_length=255)  # User that made request, if authenticated
    response_code = models.PositiveSmallIntegerField()  # Response status code
    method = models.CharField(max_length=10, null=True)  # Request method
    remote_address = models.CharField(max_length=1000, null=True)  # IP address of user
    exec_time = models.IntegerField(null=True)  # Time taken to create the response
    date = models.DateTimeField(auto_now=True)  # Date and time of request
    body_response = models.TextField(null=True)  # Response data
    body_request = models.TextField(null=True)  # Request data