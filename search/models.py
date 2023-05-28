from django.db import models






class Car(models.Model):
    make = models.CharField(max_length=100,default=None, blank=True, null=True)
    model = models.CharField(max_length=100,default=None, blank=True, null=True)
    year = models.IntegerField(default=None, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(default=None, blank=True, null=True)
    
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"



class Osoba(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    auto=models.ForeignKey(Car,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name