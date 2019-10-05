from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)


class Rating(models.Model):

    # on_delete=models.CASCADE: If object in `Movie` deleted, will remove from Rating too.
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    # To avoid rate same movie by same user
    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
