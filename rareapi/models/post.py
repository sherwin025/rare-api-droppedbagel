from unicodedata import category
from django.db import models

class Post(models.Model):
    user =models.ForeignKey("theUser", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    publication_date = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=10000)
    content = models.CharField(max_length=10000)
    approved = models.BooleanField()
    category = models.ForeignKey("category", on_delete=models.CASCADE)
    tags = models.ManyToManyField("tag", through="PostTag", related_name="taggedpost")