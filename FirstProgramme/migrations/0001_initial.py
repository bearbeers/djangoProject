# Generated by Django 4.1.7 on 2023-03-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserInfo",
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
                ("email", models.CharField(max_length=32)),
                ("password", models.CharField(max_length=64)),
                ("age", models.IntegerField()),
                ("birth", models.CharField(blank=True, max_length=20, null=True)),
                ("phone", models.CharField(blank=True, max_length=11, null=True)),
                ("remark", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
