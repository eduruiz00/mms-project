# Generated by Django 4.2.6 on 2023-12-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='bookmarked',
            field=models.BooleanField(default=False),
        ),
    ]
