# Generated by Django 2.2.5 on 2019-10-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enactuswebApp', '0005_imageupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageupload',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]