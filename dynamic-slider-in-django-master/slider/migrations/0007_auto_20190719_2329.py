# Generated by Django 2.2.2 on 2019-07-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0006_auto_20190719_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addimage',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='addimage',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
