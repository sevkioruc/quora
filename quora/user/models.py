from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Follow(models.Model):
    follower = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(
        User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return self.follower.username + ' followed ' + self.following.username
