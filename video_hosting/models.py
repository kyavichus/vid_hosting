from PIL import Image
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

from .utils import do_timestamp
from users.models import User
from django.db.models import Avg, Count


class Category(models.Model):
    FULL = 'Full'
    SAVING = 'Спасение'
    ATTACK = 'Атака'

    CAT_CHOICE = [
        (FULL, ('Полное видео')),
        (SAVING, ('Лучшее Спасение')),
        (ATTACK, ('Лучшая Атака'))
    ]

    cat_name = models.CharField(max_length=100, default="Full")
    slug = models.SlugField(max_length=255, unique=True, null=False)

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    def __str__(self):
        return self.cat_name

class Video(models.Model):

    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, default=Category.FULL)
    description = models.TextField()
    image = models.ImageField(default="image/v330w.png", upload_to='image/')
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

    def average_rating(self) -> float:
        return Rating.objects.filter(video=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def count_rating(self) -> int:
        return Rating.objects.filter(video=self).aggregate(Count("rating"))["rating__count"] or 0

    def get_absolute_url(self):
        return reverse("video", kwargs={"pk": self.id})


class Comment(models.Model):
    header = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)




class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.video.title}: {self.rating}"






