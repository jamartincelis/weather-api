# Generated by Django 3.2.7 on 2021-09-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
    ]