# Adapted from https://medium.com/@ksarthak4ever/django-custom-user-model-allauth-for-oauth-20c84888c318
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
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
    # primary key auto field
    #id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=75)
    monthly_rent = models.DecimalField(max_digits=7, decimal_places=2)
    distance = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    furnished = models.CharField(max_length=3, default="No")
    parking = models.CharField(max_length=20, default="No")
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    address = models.CharField(max_length=200)
    lat = models.FloatField(default=38.034493639911936)
    lon = models.FloatField(default=-78.50999182771713)
    services = models.TextField(default="")
    # avg_amenities = models.DecimalField(max_digits=1, decimal_places=0, default=5)
    amenities = models.TextField(default="")
    floorplan_file_name = models.CharField(max_length=100, default="/static/floorplans/floorplan.jpg")
    picture_file_name = models.CharField(max_length=100, default="/static/pictures/sample_house.jpg")
    favorite = models.ManyToManyField(User, related_name="fav_properties", blank=True)

    def __str__(self):
      if self.title == '':
        return 'This property has no title'
      else:
        return self.title

    @classmethod
    def get_property_titles(cls):
      return cls.objects.values_list('title', flat=True)

    # reference used: https://stackoverflow.com/questions/2587707/django-fix-admin-plural
    class Meta:
      verbose_name_plural = "properties"


class Review(models.Model):
    #property = models.ForeignKey(Property, related_name='ratings', blank=True, null=True,
                                # on_delete=models.CASCADE)
    property_id = models.IntegerField(default=-1)
    amenities_rating = models.IntegerField(default=0,
                                                   validators=[MaxValueValidator(5), MinValueValidator(0)]
)
    services_rating = models.IntegerField(default=0,
                                                  validators=[MaxValueValidator(5), MinValueValidator(0)]
)
    noise_level_rating = models.IntegerField(default=0,
                                                     validators=[MaxValueValidator(5), MinValueValidator(0)]
                                                     )
    text_review = models.TextField(default="", max_length=10000)
    biased_review = models.BooleanField(default=False)

# class PropertyForm(forms.Form):
#     property = models.CharField(max_length=200, default="")
#
# class RatingForm(forms.Form):
#     # properties_list = []
#     # for each in Property.objects.all():
#     #     properties_list.append((each, each))
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     properties_query = Property.get_property_titles()
#     #     #self.properties_list = []
#     #     for title in properties_query:
#     #         self.properties_list.append((title, title))
#
#     #property = TypedChoiceField(choices=properties_list, widget=RadioSelect)
#     amenities_rating = IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
#     services_rating = IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
#     noise_level_rating = IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
#

