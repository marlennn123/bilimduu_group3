from django.contrib import admin

from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Car)
class CarAdmin(TranslationAdmin):

    group_fieldsets = True

    list_display = ("city", "country", "color", "description",)


@admin.register(CarBet)
class BetAdmin(TranslationAdmin):

    group_fieldsets = True

    list_display = ("number", 'total_number')