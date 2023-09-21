from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    owner = models.ForeignKey(
        User, related_name="products", on_delete=models.CASCADE
    )


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    duration_seconds = models.PositiveIntegerField(default=0)
    products = models.ManyToManyField(Product)


class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Просмотрено", "Просмотрено"),
            ("Не просмотрено", "Не просмотрено"),
        ],
    )
