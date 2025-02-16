from django.db import models
from django.db.models import PositiveIntegerField


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
    )
    content = models.TextField(
        verbose_name="Контент",
    )
    preview = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        blank=True,
        null=True,
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")

    counter = PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
    )

    class Meta:
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"
        ordering = ["title"]

    def __str__(self):
        return self.title
