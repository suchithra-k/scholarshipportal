# Generated by Django 2.1.5 on 2019-02-03 16:29

from django.db import migrations

def insert_default_roles(apps, schema_editor):

    Role = apps.get_model('users', 'Role')
    Role.objects.create(role_id=1, role_name='admin')
    Role.objects.create(role_id=2, role_name='organisation_admin')
    Role.objects.create(role_id=3, role_name='student')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_role'),
    ]

    operations = [
        migrations.RunPython(insert_default_roles),
    ]
