from django.db import models


class Marka(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Model(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.CharField(max_length=32, verbose_name="категория")
    marka = models.ForeignKey(Marka, related_name='reviews', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name='models', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    year = models.IntegerField(default=2000)
    mileage = models.IntegerField(default=0)
    sity = models.CharField(max_length=20, verbose_name="город")
    country = models.CharField(max_length=20, verbose_name="страна")
    with_photo = models.BooleanField(default=False)
    color = models.CharField(max_length=20, verbose_name="свет")
    volume = models.FloatField(default=0)


class CarBet(models.Model):
    number = models.IntegerField(default=0)
    total_number = models.IntegerField(default=0)
    buy_now = models.IntegerField(default=0)
    start_date = models.DateTimeField
    end_date = models.DateField()