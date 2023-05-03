# Generated by Django 4.1 on 2022-12-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cartapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoardUnit",
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
                ("bname", models.CharField(max_length=20)),
                ("bgender", models.CharField(default="m", max_length=2)),
                ("bsubject", models.CharField(max_length=100)),
                ("btime", models.DateTimeField(auto_now=True)),
                ("bmail", models.EmailField(blank=True, default="", max_length=100)),
                ("bweb", models.CharField(blank=True, default="", max_length=200)),
                ("bcontent", models.TextField()),
                ("bresponse", models.TextField(blank=True, default="")),
            ],
        ),
    ]
