# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dockerterminal',
            old_name='last_udpated',
            new_name='last_updated',
        ),
        migrations.AlterField(
            model_name='dockerterminal',
            name='container_id',
            field=models.CharField(max_length=64, blank=True),
        ),
    ]
