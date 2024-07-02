# Generated by Django 5.0.6 on 2024-07-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.URLField()),
                ('on_sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
