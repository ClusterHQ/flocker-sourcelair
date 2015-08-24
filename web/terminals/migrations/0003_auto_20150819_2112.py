# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminals', '0002_auto_20150819_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dockerterminal',
            old_name='user',
            new_name='owner',
        ),
    ]
