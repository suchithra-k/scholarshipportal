# Generated by Django 2.1.5 on 2019-02-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190201_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.IntegerField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
    ]
