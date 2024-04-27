from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


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

class Review(models.Model):
    title = models.CharField(max_length = 45)
    content = models.CharField(max_length = 200)
    UserId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="UserId")
    BookId = models.ForeignKey(Book, on_delete=models.CASCADE, db_column="BookId")
    rating = models.FloatField(validators = [MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        db_table = "review"

    def __str__(self):
        return self.title
