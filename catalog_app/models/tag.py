from typing import ClassVar

from django.db import models

from main_app.enums import TagKind

DEFAULT_TAG_ORDER: int = 99

class TagManager(models.Manager):
    def get_by_natural_key(self, name: str):  # noqa: ANN201
        return self.get(name=name)

class Tag(models.Model):
    id = models.SmallAutoField('Id', primary_key=True,)
    name = models.CharField(
        'Name',
        max_length=50,
        unique=True,
    )
    label = models.CharField(
        'Label',
        max_length=50,
    )
    kind = models.PositiveSmallIntegerField(
        'Tag type',
        choices=TagKind,
    )
    order_index = models.PositiveSmallIntegerField(
        'Order',
        default=DEFAULT_TAG_ORDER
    )

    objects = TagManager()

    class Meta:
        constraints: ClassVar = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_tag_name',
            ),
        ]
        ordering = ('kind', 'order_index',)
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self) -> str:
        return f'{self.label} - {TagKind(self.kind).label}'

    def save(self, *args, **kwargs) -> None:
        self.name = str(self.name).replace(' ', '_').lower()
        super().save(*args, **kwargs)

    @property
    def pk(self) -> int: return self.id

    def natural_key(self) -> tuple[str]:
        return (self.name,)
