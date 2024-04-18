# Generated by Django 5.0.4 on 2024-04-12 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0004_alter_clients_fio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='FIO',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='procedure.user'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='procedure.status'),
        ),
    ]
