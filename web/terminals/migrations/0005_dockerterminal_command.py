# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminals', '0004_auto_20150824_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='dockerterminal',
            name='command',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
