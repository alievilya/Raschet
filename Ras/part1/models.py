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

class Page1Recogn(models.Model):
    Page1Recogn_id = models.AutoField(primary_key=True)
    chasov = models.FloatField(default = 0)
    mins = models.FloatField(default = 0)
    Trecogn = {"Page1Recogn_id": Page1Recogn_id, "chasov": chasov ,"mins": mins }

class Page1TimeMarsh(models.Model):
    Page1TimeMarsh_id = models.AutoField(primary_key=True)
    Tr = models.FloatField(default = 0)
    Trazv = {"Page1TimeMarsh_id": Page1TimeMarsh_id, "Tr": Tr }

class Page1OneWay1(models.Model):
    Page1OneWay1_id = models.AutoField(primary_key=True)
    Kir = models.FloatField(default = 0)
    OneWay1Kir = {"Page1OneWay1_id": Page1OneWay1_id, "Kir": Kir }
class Page1OneWay2(models.Model):
    Page1OneWay2_id = models.AutoField(primary_key=True)
    Kir = models.FloatField(default = 0)
    OneWay2Kir = {"Page1OneWay2_id": Page1OneWay2_id, "Kir": Kir }

class Page1CoupleWays1(models.Model):
    Page1CoupleWays1_id = models.AutoField(primary_key=True)
    Kir = models.FloatField(default = 0)
    CoupleWays1Kir = {"Page1CoupleWays1_id": Page1CoupleWays1_id, "Kir": Kir }

class Page1CoupleWays2(models.Model):
    Page1CoupleWays2_id = models.AutoField(primary_key=True)
    Kir = models.FloatField(default = 0)
    CoupleWays2Kir = {"Page1CoupleWays2_id": Page1CoupleWays2_id, "Kir": Kir }

class Part1_3(models.Model):
    part1_3_id = models.AutoField(primary_key=True)
    Nvapp = models.FloatField(default = 1)
    Nap = models.FloatField(default = 1)
    Peffpvo = models.FloatField(default = 1)
    Peffreb = models.FloatField(default = 1)
    result = models.CharField(max_length = 4, default = "")
    Out3 = {"part1_3_id": part1_3_id, "Nvapp": Nvapp, "Nap": Nap, "Peffpvo" : Peffpvo, "Peffreb" : Peffreb, "result" : result }