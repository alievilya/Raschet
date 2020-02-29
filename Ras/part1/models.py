from django.db import models
import django
from django.contrib.postgres.fields import ArrayField

class Part1(models.Model):
    part1_id = models.AutoField(primary_key=True)
    NumChastey = models.FloatField(default = 1)
    Out1 = {part1_id : "part1_id", NumChastey: "NumChastey"}

class Page1BezRazdel(models.Model):
    Page1BezRazdel_id = models.AutoField(primary_key=True)
    Kir = models.FloatField(default = 0)
    BezRazdelKir = {"Page1BezRazdel_id": Page1BezRazdel_id, "Kir": Kir }

class Part1_3(models.Model):
    part1_3_id = models.AutoField(primary_key=True)
    Nvapp = models.FloatField(default = 1)
    Nap = models.FloatField(default = 1)
    Peffpvo = models.FloatField(default = 1)
    Peffreb = models.FloatField(default = 1)
    result = models.CharField(max_length = 4, default = "")
    Out3 = {"part1_3_id": part1_3_id, "Nvapp": Nvapp, "Nap": Nap, "Peffpvo" : Peffpvo, "Peffreb" : Peffreb, "result" : result }