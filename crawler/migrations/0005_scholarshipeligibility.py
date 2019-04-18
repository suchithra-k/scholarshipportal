# Generated by Django 2.1.7 on 2019-03-17 14:08

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0004_scheduleraudit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarshipEligibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_marks', models.FloatField(null=True)),
                ('year', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('caste', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), null=True, size=None)),
                ('scholarship_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crawler.Scholarship')),
            ],
        ),
    ]
