from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = [('Male', 'Male'),('Female', 'Female')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=20, blank=True)
    group = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# create profile on default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# automating the profile
post_save.connect(create_profile, sender=User)
