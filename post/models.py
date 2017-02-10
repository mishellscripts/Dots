from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank=True, null=True, default=None)

    def __str__(self):
        return self.text
