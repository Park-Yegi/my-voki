from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    post_location = (
        ('notice', 'notice'),
        ('freeboard', 'freeboard'),
    )
    type = models.CharField(
        choices = post_location,
        max_length=20,
        default = 'freeboard',
    )

    document = models.FileField(upload_to='documents/', null=True, blank=True)
    hits = models.PositiveIntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#class User(AbstractUser):
