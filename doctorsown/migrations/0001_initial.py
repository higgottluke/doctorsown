# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParametersExtension',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('header_image_url', models.CharField(blank=True, max_length=100, null=True, default='', help_text="Enter the URL for the header image, if it's enabled.")),
                ('header_image', models.BooleanField(default=True)),
                ('extended_object', models.OneToOneField(editable=False, to='cms.Page')),
                ('public_extension', models.OneToOneField(related_name='draft_extension', null=True, editable=False, to='doctorsown.ParametersExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
