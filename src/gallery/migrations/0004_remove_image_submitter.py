# Generated by Django 3.2.5 on 2021-11-21 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='submitter',
        ),
    ]
