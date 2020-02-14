from django.db import models

class Part3(models.Model):
    part3_id = models.AutoField(primary_key=True)
    part3_heading = models.CharField(max_length=250)
    part3_body = models.TextField()

