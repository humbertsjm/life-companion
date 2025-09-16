from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class ProfileManager(models.Manager):
    def get_by_natural_key(self, name: str):  # noqa: ANN201
        return self.get(name=name)


class Profile(models.Model):
    id = models.SmallAutoField('Id', primary_key=True,)
    name = models.CharField(
        'Name',
        max_length=30,
    )
    alias = models.CharField(
        'Alias',
        max_length=50,
    )

    objects = ProfileManager()

    class Meta:
        constraints: ClassVar = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_profile_name',
            ),
        ]
        ordering = ('name',)
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self) -> str:
        return f'{self.alias}'

    def save(self, *args, **kwargs) -> None:
        self.name = str(self.name).replace(' ', '_').lower()
        super().save(*args, **kwargs)

    @property
    def pk(self) -> int: return self.id

    def natural_key(self) -> tuple[str]:
        return (self.name,)