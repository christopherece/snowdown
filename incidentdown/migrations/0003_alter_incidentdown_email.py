# Generated by Django 5.0.1 on 2024-01-30 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentdown', '0002_incidentdown_assignment_group_incidentdown_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentdown',
            name='email',
            field=models.EmailField(blank=True, db_column='emailAddress', max_length=200, null=True),
        ),
    ]
