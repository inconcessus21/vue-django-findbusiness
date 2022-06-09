from email.mime import image
from email.policy import default
import imp
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import uuid as uuid_lib
from location_field.models.plain import PlainLocationField


# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=255)
    category_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.category_name
    

class Business(models.Model):
    uuid = models.UUIDField(default=uuid_lib.uuid4, unique=True, editable=False,null=True, blank=True)
    business_name = models.CharField(max_length=255)
    image = models.ImageField(default="default.png", upload_to="upload_avatar/")
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Categories, default=1, verbose_name="category", blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    localization = PlainLocationField(based_fields=['miasto'], zoom=7, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.business_name
