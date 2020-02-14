from django.db import models


class Mainmenu(models.Model):
    mainmenu_id = models.AutoField(primary_key=True)
    mainmenu_heading = models.CharField(max_length=250)
    mainmenu_body = models.TextField()

