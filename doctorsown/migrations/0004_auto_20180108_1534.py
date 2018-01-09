# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorsown', '0003_auto_20180107_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametersextension',
            name='header_image',
            field=models.BooleanField(help_text='Enable header image. If enabled, more placeholders will appear in Structure mode.', default=False),
        ),
    ]
