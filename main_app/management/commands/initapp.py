from django.core.management.base import BaseCommand, CommandParser

from catalog_app.models import (
    Account,
    Currency,
    Tag,
)
from main_app.management.commands.seed_data import (
    get_accounts,
    get_currencies,
    get_profiles,
    get_tags,
)
from main_app.models import Profile


class Command(BaseCommand):
    help = 'Initialize app data'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Reset',
        )
        parser.add_argument(
            '--demo',
            action='store_true',
            help='Demo',
        )

    def handle(self, *args, **options) -> None:  # noqa: ARG002
        if options.get('reset', False):
            Account.objects.all().delete()
            Tag.objects.all().delete()
            Currency.objects.all().delete()
            Profile.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS('Data reseted successfully')
            )

        for p in get_profiles():
            Profile.objects.get_or_create(
                defaults={
                    'name': p.name,
                },
                alias=p.alias,
            )

        for c in get_currencies():
            Currency.objects.get_or_create(
                defaults={
                    'name': c.name,
                },
                label=c.label,
                kind=c.kind,
            )

        for t in get_tags():
            Tag.objects.get_or_create(
                defaults={
                    'name': t.name,
                },
                label=t.label,
                kind=t.kind,
                order_index=t.order_index,
            )

        for a in get_accounts():
            _owner = Profile.objects.get(name=a.owner_key)
            _currency = Currency.objects.get(name=a.currency_key)
            _tag = Tag.objects.get(name=a.tag_key)
            Account.objects.get_or_create(
                defaults={
                    'name': a.name,
                },
                label=a.label,
                owner=_owner,
                currency=_currency,
                tag=_tag,
            )

        self.stdout.write(
            self.style.SUCCESS('Data successfully initialized')
        )

        if options.get('demo', False):
            self.stdout.write(
                self.style.SUCCESS('Demo data successfully created')
            )