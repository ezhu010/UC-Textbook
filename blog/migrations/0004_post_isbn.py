# Generated by Django 2.2 on 2020-07-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200727_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isbn',
            field=models.BigIntegerField(default=0),
        ),
    ]
