# Generated by Django 2.2.2 on 2019-07-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0005_auto_20190719_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addimage',
            name='publish',
            field=models.BooleanField(null=True),
        ),
    ]
