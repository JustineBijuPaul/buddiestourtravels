# Generated by Django 4.0.5 on 2022-09-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_details_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='message',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
