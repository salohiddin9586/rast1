from django.db import models


class Lesson(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name='Назввание',
    )
    subject = models.CharField(
        max_length=120,
        verbose_name='Тема',
    )
    plan = models.TextField(
        verbose_name='План урока',
    )

    def __str__(self):
        return self.title
