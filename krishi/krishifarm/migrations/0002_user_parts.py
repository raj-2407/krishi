# Generated by Django 3.2.9 on 2021-12-07 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishifarm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='parts',
            field=models.CharField(max_length=300, null=True),
        ),
    ]