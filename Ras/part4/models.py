from django.db import models

class Part4(models.Model):
    part4_id = models.AutoField(primary_key=True)
    part4_heading = models.CharField(max_length=250)
    part4_body = models.TextField()

