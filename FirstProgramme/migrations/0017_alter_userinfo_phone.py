# Generated by Django 4.1.7 on 2023-03-18 08:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FirstProgramme", "0016_rename_phonenumber_userinfo_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="phone",
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
