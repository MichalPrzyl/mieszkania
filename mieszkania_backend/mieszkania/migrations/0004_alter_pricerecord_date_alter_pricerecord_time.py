# Generated by Django 4.1.1 on 2022-10-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mieszkania', '0003_alter_pricerecord_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricerecord',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pricerecord',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
