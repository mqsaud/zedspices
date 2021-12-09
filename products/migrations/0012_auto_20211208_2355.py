# Generated by Django 3.0.1 on 2021-12-08 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0011_auto_20211207_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rateandreview',
            old_name='review',
            new_name='user_review',
        ),
        migrations.RemoveField(
            model_name='rateandreview',
            name='status',
        ),
        migrations.RemoveField(
            model_name='rateandreview',
            name='updated_on_date',
        ),
        migrations.AlterField(
            model_name='rateandreview',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='rateandreview',
            name='rating',
            field=models.FloatField(choices=[(5, '5'), (4.5, '4.5'), (4, '4'), (3.5, '3.5'), (3, '3'), (2.5, '2.5'), (2, '2'), (1.5, '1.5'), (1, '1'), (0.5, '0.5')], default=3.5),
        ),
        migrations.AlterField(
            model_name='rateandreview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]