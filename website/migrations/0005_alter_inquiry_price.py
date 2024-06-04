# Generated by Django 5.0.4 on 2024-04-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_inquiry_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='price',
            field=models.CharField(choices=[('', 'Choose your price*'), ('1000 - 3000 USD', '1000 - 3000 USD'), ('3000 - 6000 USD', '3000 - 6000 USD'), ('6000 - 10,000 USD', '6000 - 10,000 USD'), ('Over 10,000 USD', 'Over 10,000 USD')], max_length=20),
        ),
    ]