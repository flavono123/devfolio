# Generated by Django 2.0 on 2018-02-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20180131_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='until',
            field=models.DateField(blank=True, null=True),
        ),
    ]
