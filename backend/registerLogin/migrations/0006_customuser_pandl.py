# Generated by Django 4.0.3 on 2022-04-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerLogin', '0005_remove_customuser_pandl'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pAndL',
            field=models.FloatField(default=0.0),
        ),
    ]