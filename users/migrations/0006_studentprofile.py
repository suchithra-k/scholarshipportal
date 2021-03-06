# Generated by Django 2.1.5 on 2019-02-10 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_profile_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=255)),
                ('academic_year', models.CharField(choices=[('I', 'First'), ('II', 'Second'), ('III', 'Third'), ('IV', 'Fourth'), ('V', 'Fifth')], max_length=5)),
                ('marks', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
