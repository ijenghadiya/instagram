# Generated by Django 3.2.5 on 2021-11-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_image_submitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
