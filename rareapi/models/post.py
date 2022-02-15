from django.db import models

class Post(models.Model):
    user_id = models.ForeignKey("theUser", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    publication_date = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=10000)
    content = models.CharField(max_length=10000)
    approved = models.BooleanField()
    # category = models.ManyToManyField("category", through="PostCategories", related_name="postcategory")
    # tags = models.ManyToManyField("tag", through="PostTags", related_name="posttags")
    # post_reactions = models.ManyToManyField("reaction", through="post_reactions", related_name="post_reactions")