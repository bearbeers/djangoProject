# Generated by Django 4.1.7 on 2023-03-18 07:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("FirstProgramme", "0012_alter_userinfo_dateofbirth"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userinfo",
            name="dateofbirth",
        ),
    ]