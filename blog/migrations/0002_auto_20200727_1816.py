# Generated by Django 2.2 on 2020-07-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Like New', 'Like New'), ('Fair', 'Fair'), ('Poor', 'Poor')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='course',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='textbook/default.jpg', upload_to='textbook'),
        ),
        migrations.AddField(
            model_name='post',
            name='professor',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='school',
            field=models.CharField(choices=[('UC Irvine', 'UC Irvine'), ('UC Riverside', 'UC Riverside'), ('UC Davis', 'UC Davis'), ('UC Berkeley', 'UC Berkeley'), ('UC San Diego', 'UC San Diego'), ('UC Santa Barbara', 'UC Santa Barbara'), ('UC Merced', 'UC Merced'), ('UC Los Angeles', 'UC Los Angeles'), ('UC Santa Cruz', 'UC Santa Cruz')], default='---------', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='title_of_textbook',
            field=models.CharField(default='', max_length=50),
        ),
    ]
