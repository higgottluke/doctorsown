# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorsown', '0002_auto_20180107_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parametersextension',
            name='header_image_url',
        ),
        migrations.AlterField(
            model_name='parametersextension',
            name='header_image',
            field=models.BooleanField(help_text='Enable header image. If enabled, more placeholders will appear in Structure mode.', default=True),
        ),
    ]
