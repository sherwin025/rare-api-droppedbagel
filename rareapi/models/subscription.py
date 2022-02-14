from django.db import models
from datetime import datetime


class Subscription(models.Model):
    follower_id = models.IntegerField()
    author_id = models.IntegerField()
    created_on = models.DateField(auto_now=False, auto_now_add=False)