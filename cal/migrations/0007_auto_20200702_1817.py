# Generated by Django 3.0.7 on 2020-07-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0006_auto_20200702_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]
