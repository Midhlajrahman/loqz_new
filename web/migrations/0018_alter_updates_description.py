# Generated by Django 5.0.2 on 2024-03-27 10:55

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_productfeature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
