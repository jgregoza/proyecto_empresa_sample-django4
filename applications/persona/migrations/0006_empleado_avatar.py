# Generated by Django 4.0.2 on 2022-02-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
