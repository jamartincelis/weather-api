# Generated by Django 3.2.7 on 2021-09-08 18:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('transaction_date', models.DateTimeField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.code')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
            options={
                'db_table': 'transactions',
                'managed': True,
            },
        ),
    ]
