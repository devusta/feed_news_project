# Generated by Django 5.0 on 2024-05-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_customuser_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
