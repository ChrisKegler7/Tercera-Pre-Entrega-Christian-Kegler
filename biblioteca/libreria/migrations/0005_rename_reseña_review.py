# Generated by Django 5.0.6 on 2024-07-02 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_cliente_reseña_delete_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reseña',
            new_name='Review',
        ),
    ]
