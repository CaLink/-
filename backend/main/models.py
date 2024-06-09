from django.db import models

class Car(models.Model):
    auction = models.CharField(max_length=128, blank=False, null=False)
    car_id = models.IntegerField()
    sub_brand_name = models.CharField(max_length=128, blank=True, null=True)
    official_price = models.CharField(max_length=128, blank=True, null=True)
    fuel_form = models.CharField(max_length=128, blank=True, null=True)
    market_time = models.CharField(max_length=128, blank=True, null=True)
    engine_description = models.CharField(max_length=128, blank=True, null=True)
    energy_elect_max_power = models.CharField(max_length=128, blank=True, null=True)
    gearbox_description = models.CharField(max_length=128, blank=True, null=True)

class Analytics(models.Model):
    action = models.CharField(max_length=128)

    def __str__(self):
        return self.action   
    
class Logs(models.Model):
    dt = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=512)
    file = models.CharField(max_length=512)
    row = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.dt} - {self.type}'