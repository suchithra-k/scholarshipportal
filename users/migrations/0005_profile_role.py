# Generated by Django 2.1.5 on 2019-02-03 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190203_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='users.Role'),
        ),
    ]
