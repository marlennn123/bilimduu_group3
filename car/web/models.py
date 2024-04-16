from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.title


class Marka(models.Model):
    title = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=255, verbose_name="модель", null=True)
    marka = models.ForeignKey(Marka, related_name='marka', on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=0, null=True)
    year = models.IntegerField(default=2000, null=True)
    mileage = models.IntegerField(default=0, null=True)
    city = models.CharField(max_length=20, verbose_name="город", null=True)
    country = models.CharField(max_length=20, verbose_name="страна", null=True)
    with_photo = models.BooleanField(default=False, null=True)
    color = models.CharField(max_length=20, verbose_name="свет", null=True)
    volume = models.FloatField(default=0, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


class CarBet(models.Model):
    number = models.IntegerField(default=0, null=True)
    total_number = models.IntegerField(default=0, null=True)
    buy_now = models.IntegerField(default=0, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)