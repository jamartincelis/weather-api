from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'cities'
        managed = True
