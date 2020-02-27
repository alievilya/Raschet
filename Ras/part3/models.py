from django.db import models
import django
from django.contrib.postgres.fields import ArrayField

class Part3(models.Model):
    part3_id = models.AutoField(primary_key=True)
    Elements = models.FloatField(default = 1)
    Out1 = {"Elements": Elements}

class Part3_2(models.Model):
    part3_2_id = models.AutoField(primary_key=True)
    Sc = models.FloatField(default = 1)
    Smax = models.FloatField(default = 1)
    result = models.CharField(max_length = 4, default = "")
    Out2 = {"part3_2_id": part3_2_id, "Sc": Sc, "Smax": Smax, "result": result }

class Part3_3(models.Model):
    part3_3_id = models.AutoField(primary_key=True)
    Nvapp = models.FloatField(default = 1)
    Nap = models.FloatField(default = 1)
    Peffpvo = models.FloatField(default = 1)
    Peffreb = models.FloatField(default = 1)
    result = models.CharField(max_length = 4, default = "")
    Out3 = {"part3_3_id": part3_3_id, "Nvapp": Nvapp, "Nap": Nap, "Peffpvo" : Peffpvo, "Peffreb" : Peffreb, "result" : result }