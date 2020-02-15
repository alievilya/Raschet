from django.db import models

class Part4(models.Model):
    part4_id = models.AutoField(primary_key=True)
    line_selected = models.FloatField(default = 0)
    canal_selected = models.FloatField(default = 0)
    number_val = models.FloatField(default = 0)


