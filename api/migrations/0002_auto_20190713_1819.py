# Generated by Django 2.2.3 on 2019-07-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metrics',
            name='date',
            field=models.DateField(),
        ),
    ]
