from django.db import models

class Comment(models.Model):
    user = models.ForeignKey("theUser", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)