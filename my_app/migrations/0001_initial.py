# Generated by Django 3.0.5 on 2020-04-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_field', models.CharField(max_length=500)),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
