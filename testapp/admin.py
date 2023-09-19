from django.contrib import admin
from reversion.admin import VersionAdmin
from reversion_compare.admin import CompareVersionAdmin

from . import models

# @admin.register(models.Poll)
# class PollAdmin(VersionAdmin):
#     pass


# @admin.register(models.Choice)
# class ChoiceAdmin(VersionAdmin):
#     pass


@admin.register(models.Poll)
class PollAdmin(CompareVersionAdmin):
    pass


@admin.register(models.Choice)
class ChoiceAdmin(CompareVersionAdmin):
    pass
