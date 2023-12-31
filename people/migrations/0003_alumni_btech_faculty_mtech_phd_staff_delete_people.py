# Generated by Django 4.1.5 on 2023-04-04 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0002_alter_people_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Alumni",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("roll_no", models.CharField(max_length=50)),
                ("program", models.CharField(max_length=10000)),
                ("date", models.CharField(max_length=50)),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("year", models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name="BTech",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("roll_no", models.CharField(max_length=50)),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("year", models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("details", models.CharField(max_length=10000)),
                ("address", models.CharField(blank=True, max_length=500)),
                ("link", models.URLField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="MTech",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("roll_no", models.CharField(max_length=50)),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("year", models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name="Phd",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("roll_no", models.CharField(max_length=50)),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("details", models.CharField(blank=True, max_length=1000)),
                ("year", models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("image", models.ImageField(blank=True, upload_to="")),
            ],
        ),
        migrations.DeleteModel(
            name="People",
        ),
    ]
