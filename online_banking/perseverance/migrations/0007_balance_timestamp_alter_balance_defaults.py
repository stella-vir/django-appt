# Generated by Django 4.1 on 2022-09-15 19:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('perseverance', '0006_alter_balance_defaults_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Transaction timestamp '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='balance',
            name='defaults',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=20),
        ),
    ]
