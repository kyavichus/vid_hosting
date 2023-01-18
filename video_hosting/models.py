from django.core.validators import FileExtensionValidator
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    vid = models.ForeignKey('Video', on_delete=models.PROTECT, null=True)
    rate = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'rating = {self.rate}'

