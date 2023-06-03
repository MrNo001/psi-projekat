from django.db import models

from django.contrib.auth.models import User



class Offer(models.Model):

    BODY_TYPES=[
        ("L","Limunzina"),
        ("K","Karavan")
    ]


    name = models.CharField(max_length=255)
    model= models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    godiste = models.IntegerField(default=0)
    is_premium = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='offers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    body= models.CharField(choices=BODY_TYPES,default="L",max_length=1)
    
    def __str__(self):
        return self.name



class Picture(models.Model):
    image = models.ImageField(upload_to='car_images', blank=True, null=True)
    offer= models.ForeignKey(Offer,related_name='pictures',on_delete=models.CASCADE)
