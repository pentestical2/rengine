# Generated by Django 3.2.4 on 2021-10-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0006_auto_20211030_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaininfo',
            name='date_created',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='domaininfo',
            name='domain_age',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]