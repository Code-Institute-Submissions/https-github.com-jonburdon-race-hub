# Generated by Django 3.1.1 on 2020-10-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20201001_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='racehubfriends',
            name='myfriendsracehubid',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
