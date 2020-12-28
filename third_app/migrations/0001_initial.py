# Generated by Django 3.1.4 on 2020-12-24 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
