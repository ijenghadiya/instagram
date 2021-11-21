# Generated by Django 3.2.5 on 2021-11-21 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20211121_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_caption', to='gallery.caption'),
        ),
    ]
