# Generated by Django 2.2.3 on 2019-10-06 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20191006_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='justimage',
        ),
        migrations.DeleteModel(
            name='JustImages',
        ),
    ]
