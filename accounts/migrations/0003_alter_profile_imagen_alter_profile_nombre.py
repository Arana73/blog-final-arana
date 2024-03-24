# Generated by Django 5.0.2 on 2024-03-22 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_descripcion_profile_imagen_profile_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
