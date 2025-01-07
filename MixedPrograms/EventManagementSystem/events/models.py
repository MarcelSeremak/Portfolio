from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=350)

    def __str__(self):
        return self.comment

class Event(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    place = models.CharField(max_length=300)
    time = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True)
    tickets_amount = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)