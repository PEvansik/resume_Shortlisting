# Generated by Django 3.2.3 on 2022-04-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0011_auto_20191022_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RightExperience', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
