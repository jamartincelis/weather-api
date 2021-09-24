# Generated by Django 3.2.7 on 2021-09-24 14:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
            options={
                'db_table': 'accounts',
                'managed': True,
            },
        ),
    ]
