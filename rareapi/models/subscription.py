from django.db import models
from datetime import datetime


class Subscription(models.Model):
    follower = models.ForeignKey("theUser", on_delete=models.CASCADE, related_name="sub_follower")
    author = models.ForeignKey("theUser", on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True, auto_now_add=False)