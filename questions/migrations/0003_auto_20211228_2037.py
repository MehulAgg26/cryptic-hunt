# Generated by Django 2.2.5 on 2021-12-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20180114_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='hint',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='question',
            field=models.CharField(max_length=5000),
        ),
    ]
