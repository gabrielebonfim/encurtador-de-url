# Generated by Django 4.0.2 on 2022-02-26 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_encourter', '0002_alter_url_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='data_expiracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]