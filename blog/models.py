from django.db import models
from django.contrib.auth.models import User


# keep draft and published posts separated when we render them out with templates
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # specify descending order using the negative prefix
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
