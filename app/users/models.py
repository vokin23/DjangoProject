from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    about = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username