# Generated by Django 2.0.1 on 2018-02-18 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_auto_20180218_0211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailcode',
            options={'verbose_name_plural': '临时邮箱验证码'},
        ),
        migrations.AlterModelTable(
            name='emailcode',
            table='EmailCode',
        ),
    ]