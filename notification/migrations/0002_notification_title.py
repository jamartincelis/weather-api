# Generated by Django 3.2.7 on 2021-11-18 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='title',
            field=models.CharField(default=None, max_length=60),
            preserve_default=False,
        ),
    ]