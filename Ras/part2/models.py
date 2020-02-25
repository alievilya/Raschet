from django.db import models
from django.db import models
import django
from django.contrib.postgres.fields import ArrayField


class Part2(models.Model):
    part2_id = models.AutoField(primary_key=True)
    Nel = models.FloatField(default = 1)
    res1 = {"Nel": Nel}


class Part2_2(models.Model):


    part2_2_id = models.AutoField(primary_key=True)
    Nvskrap = models.FloatField(default = 1)
    Napp = models.FloatField(default = 1)
    result = models.CharField(max_length = 4, default = "")
    #res2 = {"part2_2_id": part2_2_id, "Nvskrap": Nvskrap, "Napp": Napp, "result": result}
    res2 = {"part2_2_id": part2_2_id, "Nvskrap": Nvskrap, "Napp": Napp, "result": result }
