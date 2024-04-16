from .models import Car, CarBet
from modeltranslation.translator import TranslationOptions,register


@register(Car)
class ProductTranslationOptions(TranslationOptions):
    fields = ('city', 'country', 'color', 'description')


@register(CarBet)
class ProductTranslationOptions(TranslationOptions):
    fields = ('number', 'total_number')