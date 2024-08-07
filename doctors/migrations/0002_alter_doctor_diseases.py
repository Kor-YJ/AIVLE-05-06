# Generated by Django 5.0.6 on 2024-07-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("departments", "0003_alter_departments_diseases"),
        ("doctors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="diseases",
            field=models.ManyToManyField(blank=True, to="departments.disease"),
        ),
    ]
