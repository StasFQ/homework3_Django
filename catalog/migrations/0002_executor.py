# Generated by Django 4.1.2 on 2022-10-28 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='catalog.city')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
