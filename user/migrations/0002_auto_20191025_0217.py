# Generated by Django 2.2.2 on 2019-10-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(blank=True, default='img/db_234.gif', max_length=100, null=True, verbose_name='avatar'),
        ),
    ]
