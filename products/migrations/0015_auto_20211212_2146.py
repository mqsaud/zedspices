# Generated by Django 3.0.1 on 2021-12-12 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20211209_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rateandreview',
            options={'ordering': ['-created_on_date']},
        ),
    ]
