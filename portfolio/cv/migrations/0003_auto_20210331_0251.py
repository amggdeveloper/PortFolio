# Generated by Django 3.1.7 on 2021-03-31 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20210331_0251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto',
            options={'ordering': ('fecha',)},
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='created',
        ),
    ]
