# Generated by Django 5.0.4 on 2024-05-10 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elementdb',
            old_name='email',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='elementdb',
            old_name='password',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='elementdb',
            name='place',
        ),
    ]
