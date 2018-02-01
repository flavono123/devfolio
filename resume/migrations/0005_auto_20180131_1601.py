# Generated by Django 2.0 on 2018-01-31 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20180131_1523'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Eduction',
            new_name='Education',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='mail',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='link',
            name='blog',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='link',
            name='github',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='link',
            name='google_plus',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='link',
            name='linkedin',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='link',
            name='stackoverflow',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='link',
            name='twitter',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
