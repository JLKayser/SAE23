# Generated by Django 4.0.5 on 2022-06-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0002_alter_produit_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.BigIntegerField(default='0'),
        ),
    ]