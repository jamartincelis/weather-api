# Generated by Django 4.0 on 2022-05-23 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_rename_budget_amount_budget_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget',
            old_name='budget_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='budget',
            old_name='budget_status',
            new_name='status',
        ),
    ]
