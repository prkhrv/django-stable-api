# Generated by Django 3.1.5 on 2021-02-09 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_student_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoccerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
            ],
        ),
    ]
