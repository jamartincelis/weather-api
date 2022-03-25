# Generated by Django 4.0 on 2022-03-21 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget',
            old_name='category',
            new_name='category_id',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='user',
        ),
        migrations.AddField(
            model_name='budget',
            name='created_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='status_id',
            field=models.UUIDField(db_index=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='user_id',
            field=models.UUIDField(db_index=True, default=None, null=True),
        ),
    ]