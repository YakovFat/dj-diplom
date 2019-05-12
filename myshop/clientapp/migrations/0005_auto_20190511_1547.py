# Generated by Django 2.1.3 on 2019-05-11 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0004_auto_20190510_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('date_creation',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='order',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]