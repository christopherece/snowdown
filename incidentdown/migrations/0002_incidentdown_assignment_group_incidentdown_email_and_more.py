# Generated by Django 5.0.1 on 2024-01-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentdown', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentdown',
            name='assignment_group',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='incidentdown',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='incidentdown',
            name='impact',
            field=models.CharField(default='1 - 4 Users', max_length=200),
        ),
        migrations.AddField(
            model_name='incidentdown',
            name='state',
            field=models.CharField(default='New', max_length=200),
        ),
        migrations.AddField(
            model_name='incidentdown',
            name='urgency',
            field=models.CharField(default='Impeding normal work', max_length=200),
        ),
        migrations.AddField(
            model_name='incidentdown',
            name='worknotes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incidentdown',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incidentdown',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
