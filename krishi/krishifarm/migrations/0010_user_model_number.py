# Generated by Django 3.2.9 on 2021-12-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishifarm', '0009_remove_user_model_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='model_number',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
