# Generated by Django 2.0.4 on 2018-05-02 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='andress',
            new_name='address',
        ),
        migrations.AddField(
            model_name='dish',
            name='rating',
            field=models.PositiveIntegerField(default=4),
            preserve_default=False,
        ),
    ]
