# Generated by Django 5.0.6 on 2024-07-05 01:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("consultations", "0002_alter_consultation_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="detailconsultation",
            options={"verbose_name": "세부진료", "verbose_name_plural": "세부진료들"},
        ),
    ]
