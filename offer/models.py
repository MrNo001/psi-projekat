from django.db import models

from django.contrib.auth.models import User


class Offer(models.Model):

    BODY_TYPES = [
        ("L", "Limunzina"),
        ("H", "Hečbek"),
        ("K", "Karavan"),
    ]

    GEARBOX_TYPES = [
        ("M", "Manuelni"),
        ("A", "Automatski"),
    ]

    FUEL_TYPES = [
        ("B", "Benzin"),
        ("D", "Dizel"),
        ("G", "Gas (TNG)"),
        ("E", "Električni pogon"),
        ("H", "Hibridni pogon"),
    ]


    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    body_type = models.CharField(choices=BODY_TYPES, default="L", max_length=1)
    fuel_type = models.CharField(choices=FUEL_TYPES, default="B", max_length=1)
    gearbox = models.CharField(choices=GEARBOX_TYPES, default="M", max_length=1)
    power = models.IntegerField(default=0)

    price = models.FloatField(default=0)

    created_by = models.ForeignKey(User, related_name='offers', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_premium = models.BooleanField(default=False)

    subscribers = models.ManyToManyField(User)

    
    def __str__(self):
        return self.name



class Picture(models.Model):
    image = models.ImageField(upload_to='user_images', blank=True, null=True)
    offer = models.ForeignKey(Offer, related_name='pictures', on_delete=models.CASCADE, null=True)

