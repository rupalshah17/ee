# Generated by Django 4.1 on 2023-08-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0012_alter_faculty_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="faculty",
            name="place",
            field=models.CharField(default="1.0", max_length=50),
            preserve_default=False,
        ),
    ]
