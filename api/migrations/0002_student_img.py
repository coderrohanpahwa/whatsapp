# Generated by Django 3.1.3 on 2020-12-07 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(default=' ', upload_to='api/static/images'),
            preserve_default=False,
        ),
    ]
