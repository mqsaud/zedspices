# Generated by Django 3.0.1 on 2021-12-07 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20211207_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rateandreview',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
