# Generated by Django 2.0.7 on 2018-09-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20180906_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
