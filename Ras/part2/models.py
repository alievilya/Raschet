from django.db import models
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Part2(models.Model):
    part2_id = models.AutoField(primary_key=True)
    Nel = models.FloatField(default = 1)
    res1 = {"Nel": Nel}


class Part2_2(models.Model):
    part2_2_id = models.AutoField(primary_key=True)
    Nvskrap = models.FloatField(default = 1)
    Napp = models.FloatField(default = 1)

    #Nvskrap = models.CharField(max_length = 5)
    #massive = ArrayField(
    #        ArrayField(
    #            models.FloatField(max_length=3, blank=True),
    #            size=8,
    #        ),
     #       size=2,
     #   )
    res2 = {"Nvskrap": Nvskrap, "Napp": Napp}

