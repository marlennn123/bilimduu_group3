from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Marka(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=32)
    marka = models.ForeignKey(Marka, related_name='marka', on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=0)
    year = models.IntegerField(default=2000)
    mileage = models.IntegerField(default=0)
    city = models.CharField(max_length=20, verbose_name="город")
    country = models.CharField(max_length=20, verbose_name="страна")
    with_photo = models.BooleanField(default=False)
    color = models.CharField(max_length=20, verbose_name="свет")
    volume = models.FloatField(default=0)

    def __str__(self):
        return self.title


class CarBet(models.Model):
    number = models.IntegerField(default=0)
    total_number = models.IntegerField(default=0)
    buy_now = models.IntegerField(default=0)
    start_date = models.DateTimeField
    end_date = models.DateField()