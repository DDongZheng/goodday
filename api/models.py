from django.db import models

class GoodDeed(models.Model):
    content = models.TextField()
    likes_count = models.PositiveIntegerField(default=0)
    not_good_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50]

# Create your models here.
