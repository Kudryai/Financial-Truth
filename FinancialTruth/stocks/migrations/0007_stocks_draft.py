# Generated by Django 4.1.1 on 2022-09-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_alter_stocks_country_alter_stocks_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Больше не в индексе'),
        ),
    ]
