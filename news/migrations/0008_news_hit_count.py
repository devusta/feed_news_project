# Generated by Django 5.0 on 2024-06-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0007_rename_active_comment_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="hit_count",
            field=models.IntegerField(default=0),
        ),
    ]
