from django.db import models


class PostImage(models.Model):
    post = models.ForeignKey("Post", on_delete=models.DO_NOTHING, related_name='pictures')
    postimage = models.ImageField(
        upload_to='actionimages', height_field=None,
        width_field=None, max_length=None, null=True)