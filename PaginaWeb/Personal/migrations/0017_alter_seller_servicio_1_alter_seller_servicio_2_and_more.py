# Generated by Django 4.2.5 on 2023-09-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0016_alter_personal_permisos_alter_personal_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='servicio_1',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='servicio_2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='servicio_3',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='servicio_4',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
