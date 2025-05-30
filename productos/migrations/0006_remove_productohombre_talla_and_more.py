# Generated by Django 4.2 on 2025-04-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_productohombre_productomujer_productonino_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productohombre',
            name='talla',
        ),
        migrations.RemoveField(
            model_name='productomujer',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productonino',
            name='edad_recomendada',
        ),
        migrations.AddField(
            model_name='productohombre',
            name='imagen_url',
            field=models.CharField(default='imagenes/default.jpg', max_length=255),
        ),
        migrations.AddField(
            model_name='productomujer',
            name='imagen_url',
            field=models.CharField(default='imagenes/default.jpg', max_length=255),
        ),
        migrations.AddField(
            model_name='productonino',
            name='imagen_url',
            field=models.CharField(default='imagenes/default.jpg', max_length=255),
        ),
    ]
