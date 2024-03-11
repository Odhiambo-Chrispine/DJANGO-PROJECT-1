# Generated by Django 5.0.3 on 2024-03-10 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='issued_by_internally',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='items',
            name='issued_from_internally',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='items',
            name='issued_to_internally',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
