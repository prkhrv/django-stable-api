# Generated by Django 3.1.5 on 2021-02-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
