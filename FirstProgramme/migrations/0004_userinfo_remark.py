# Generated by Django 4.1.7 on 2023-03-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FirstProgramme", "0003_userinfo_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="remark",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]