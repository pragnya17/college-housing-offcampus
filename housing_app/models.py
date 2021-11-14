# Adapted from https://medium.com/@ksarthak4ever/django-custom-user-model-allauth-for-oauth-20c84888c318
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=75)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    distance = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    furnished = models.CharField(max_length=3, default="No")
    parking = models.CharField(max_length=20, default="No")
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    address = models.CharField(max_length=200)
    services = models.TextField(default="")
    amenities = models.TextField(default="")
    favorite = models.BooleanField(default=False)
    floorplan = models.ImageField(upload_to='floorplans')
    picture = models.ImageField(upload_to='pictures', default="")

    def __str__(self):
      if self.title == '':
        return 'This property has no title'
      else:
        return self.title
    
    # reference used: https://stackoverflow.com/questions/2587707/django-fix-admin-plural
    class Meta:
      verbose_name_plural = "properties"

#  TODO
# class Review(models.Model):
#     property = models.ForeignKey(Property, on_delete=models.CASCADE)
#     review_text = models.TextField()
#     upvotes = models.IntegerField(default=0)
