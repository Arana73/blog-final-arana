# Generated by Django 5.0.2 on 2024-03-29 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
