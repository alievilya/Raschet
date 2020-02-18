from django.db import models

class Part4(models.Model):
    part4_id = models.AutoField(primary_key=True)
    line_selected = models.FloatField(default = 6)
    canal_selected = models.FloatField(default = 2)
    number_val = models.FloatField(default = 1)
    cur = {"line_selected": line_selected, "canal_selected": canal_selected, "number_val": number_val}


