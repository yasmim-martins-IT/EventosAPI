# Generated by Django 5.1.7 on 2025-03-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_alter_eventos_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='data',
            field=models.DateField(),
        ),
    ]
