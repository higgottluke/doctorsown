# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('doctorsown', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametersextension',
            name='header_image_url',
            field=filer.fields.image.FilerImageField(help_text="Enter the URL for the header image, if it's enabled.", blank=True, to=settings.FILER_IMAGE_MODEL, null=True),
        ),
    ]
