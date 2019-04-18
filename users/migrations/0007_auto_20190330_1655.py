# Generated by Django 2.1.7 on 2019-03-30 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_studentprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='caste',
            field=models.CharField(choices=[('', '---'), ('OC', 'OC'), ('BC', 'BC'), ('MBC', 'MBC'), ('BCM', 'BCM'), ('SC', 'SC'), ('ST', 'ST')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='academic_year',
            field=models.IntegerField(choices=[(0, '---'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth')], null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='course',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='degree',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='marks',
            field=models.FloatField(null=True),
        ),
    ]
