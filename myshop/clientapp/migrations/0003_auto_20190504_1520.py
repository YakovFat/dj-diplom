# Generated by Django 2.1.3 on 2019-05-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0002_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='product',
        ),
        migrations.AddField(
            model_name='article',
            name='product',
            field=models.ManyToManyField(blank=True, to='clientapp.Product'),
        ),
    ]