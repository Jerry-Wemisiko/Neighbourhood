# Generated by Django 3.2.7 on 2021-09-28 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magiccity', '0002_rename_name_business_bizz_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='neighbourhood_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='neighbourhood_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='neighbourhood_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='admin',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='neighbourhood_photo',
        ),
    ]
