from django.db import models

# Create your models here.
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
