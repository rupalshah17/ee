# Generated by Django 4.1.5 on 2023-04-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("research", "0003_research_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="papers",
            name="paper",
            field=models.CharField(max_length=500),
        ),
    ]
