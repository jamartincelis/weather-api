# Generated by Django 3.2.7 on 2021-11-16 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tip', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tip',
            old_name='name',
            new_name='title',
        ),
    ]