# Generated by Django 5.1.2 on 2024-11-01 04:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_remove_shortenedurl_complate_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenedurl',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shortenedurl',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='shortenedurl',
            name='status',
            field=models.PositiveIntegerField(choices=[(0, 'CONVERTED'), (1, 'PENDING'), (2, 'FAILED')], default=0),
        ),
    ]