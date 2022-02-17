from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class theUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    created_on = models.DateField(auto_now=True, auto_now_add=False)
    profile_pic = models.ImageField(
        upload_to='profileimages', height_field=None,
        width_field=None, max_length=None, null=True)

# class userPicture(models.Model):
#     user = models.ForeignKey(theUser, on_delete=models.DO_NOTHING, related_name="pictures")
#     profile_pic = models.ImageField(
#         upload_to='profileimages', height_field=None,
#         width_field=None, max_length=None, null=True)