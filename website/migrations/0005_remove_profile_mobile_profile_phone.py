# Generated by Django 5.1.1 on 2024-10-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_contact_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mobile',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
