# Generated by Django 3.2.3 on 2022-04-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0012_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='RightSkills',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='feedback',
            name='resumeId',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
