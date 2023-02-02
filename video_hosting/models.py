from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from .utils import do_timestamp


class Video(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default=" image/v330w.png", upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        do_timestamp(self.image.path)


class Rating(models.Model):
    vid = models.ForeignKey('Video', on_delete=models.CASCADE, null=True)
    rate = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'rating = {self.rate}'




