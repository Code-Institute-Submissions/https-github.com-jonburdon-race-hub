# Generated by Django 3.1.1 on 2020-10-19 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0019_auto_20201016_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='dateofbirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]