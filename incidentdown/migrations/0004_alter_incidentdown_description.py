# Generated by Django 5.0.1 on 2024-01-30 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentdown', '0003_alter_incidentdown_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentdown',
            name='description',
            field=models.TextField(blank=True, db_column='description', null=True),
        ),
    ]
