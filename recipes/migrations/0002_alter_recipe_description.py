# Generated by Django 5.1.3 on 2024-11-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
