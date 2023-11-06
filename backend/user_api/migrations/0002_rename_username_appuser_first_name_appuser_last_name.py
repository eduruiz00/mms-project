# Generated by Django 4.2.6 on 2023-10-30 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='username',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(default='Last name', max_length=100),
            preserve_default=False,
        ),
    ]