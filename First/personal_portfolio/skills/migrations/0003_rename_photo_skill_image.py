# Generated by Django 4.2.6 on 2023-10-20 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_rename_image_skill_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='photo',
            new_name='image',
        ),
    ]
