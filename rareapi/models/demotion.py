from django.db import models

class Demotion(models.Model):
    user = models.ForeignKey("theUser", on_delete=models.CASCADE, related_name="demotions")
    first_approver = models.ForeignKey("theUser", on_delete=models.CASCADE)
    deactivate = models.BooleanField()
    demote = models.BooleanField()