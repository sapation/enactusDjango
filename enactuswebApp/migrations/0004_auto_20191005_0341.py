# Generated by Django 2.2.5 on 2019-10-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enactuswebApp', '0003_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateField(auto_now=True),
        ),
    ]
