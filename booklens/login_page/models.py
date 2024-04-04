from django.db import models
from django.core.validators import MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=65)
    author = models.CharField(max_length=65, null=True, blank=True)
    publisher = models.CharField(max_length=65, null=True, blank=True)
    publication_year = models.PositiveSmallIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(9999)]
    )
    genre = models.CharField(max_length=65, null=True, blank=True)
    cover_image_path = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.title
