# Generated by Django 3.0.7 on 2020-07-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_remove_reader_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='start_time',
            field=models.DateTimeField(verbose_name='Дата регистрации'),
        ),
    ]
