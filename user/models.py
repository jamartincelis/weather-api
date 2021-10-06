import uuid

from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    optional_id = models.CharField(max_length=60, blank=True)
    email = models.EmailField(null=True, default=None, blank=True)

    class Meta:
        managed = True
        db_table = 'users'

    def __str__(self):
        return str(self.id)
