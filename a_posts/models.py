import uuid
from django.db import models


class Post(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    artist = models.CharField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)
    title = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    body = models.TextField()
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created_at']


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return str(self.name)