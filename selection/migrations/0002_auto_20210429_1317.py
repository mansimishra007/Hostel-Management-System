# Generated by Django 2.1.2 on 2021-04-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='no_dues',
            field=models.BooleanField(default=False),
        ),
    ]
