from django.contrib import admin

from .models import Account, Currency, Tag

admin.site.register(Account)
admin.site.register(Currency)
admin.site.register(Tag)
