from django.db import models

class Part4(models.Model):
    part4_id = models.AutoField(primary_key=True)
    line_selected = models.FloatField(default = 6)
    canal_selected = models.FloatField(default = 2)
    number_val = models.FloatField(default = 1)
    cur = {"line_selected": line_selected, "canal_selected": canal_selected, "number_val": number_val}


class Part4_2(models.Model):
    part4_2_id = models.AutoField(primary_key=True)
    mestnost_selected = models.FloatField(default = 1)
    temp_val = models.FloatField(default = 25)
    snow_val = models.FloatField(default = 0)
    wind_val = models.FloatField(default = 3)
    all = {"mestnost_selected": mestnost_selected, "temp_val": temp_val, "snow_val": snow_val,
    "wind_val": wind_val}


class Part4_3(models.Model):
    part4_3_id = models.AutoField(primary_key=True)
    stanciya_selected = models.FloatField(default = 60)
    marsh_val = models.FloatField(default = 10)
    full = {"stanciya_selected": stanciya_selected, "marsh_val": marsh_val}