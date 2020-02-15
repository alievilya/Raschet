from django.db import models

class Part4(models.Model):
    part4_id = models.AutoField(primary_key=True)
    part4_line = models.FloatField(default = 0)
    part4_canal = models.FloatField(default = 0)
    part4_number_val = models.FloatField(default = 0)


