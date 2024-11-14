# Generated by Django 5.1.2 on 2024-10-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='hotel_stars',
        ),
        migrations.AddField(
            model_name='hotel',
            name='stars',
            field=models.PositiveSmallIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='Рейтинг'),
            preserve_default=False,
        ),
    ]
