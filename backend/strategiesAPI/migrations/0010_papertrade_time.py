# Generated by Django 4.0.4 on 2022-06-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategiesAPI', '0009_papertrade_iscompleted_papertrade_stop_loss_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='papertrade',
            name='time',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
