from typing import ClassVar

from django.db import models

from main_app.models import Profile

from .currency import Currency
from .tag import Tag

UNCODED_ACCOUNT: int = 999


class AccountManager(models.Manager):
    def get_by_natural_key(self, name: str):  # noqa: ANN201
        return self.get(name=name)


class Account(models.Model):
    id = models.SmallAutoField(
        'Id',
        primary_key=True,
    )
    code = models.PositiveSmallIntegerField(
        'Code',
        default=UNCODED_ACCOUNT
    )
    name = models.CharField(
        'Name',
        max_length=50,
    )
    label = models.CharField(
        'Label',
        max_length=50,
    )
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.PROTECT,
    )
    currency = models.ForeignKey(
        to=Currency,
        on_delete=models.PROTECT,
    )
    tag = models.ForeignKey(
        to=Tag,
        on_delete=models.PROTECT,
    )

    objects = AccountManager()

    class Meta:
        constraints: ClassVar = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_account_name',
            ),
        ]
        ordering = ('owner', 'code',)
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self) -> str:
        return f'{self.label} - {self.currency.label}'

    def save(self, *args, **kwargs) -> None:
        self.name = str(self.name).replace(' ', '_').lower()
        super().save(*args, **kwargs)

    @property
    def pk(self) -> int: return self.id

    def natural_key(self) -> tuple[str]:
        return (self.name,)