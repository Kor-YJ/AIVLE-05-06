# Generated by Django 5.0.6 on 2024-07-05 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consultations", "0001_initial"),
        ("doctors", "0003_alter_doctor_options_alter_doctor_departments_id_and_more"),
        ("patients", "0002_alter_patient_options_alter_patient_patient_bday_and_more"),
        ("reservations", "0002_alter_reservation_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="consultation",
            options={"verbose_name": "진료", "verbose_name_plural": "진료들"},
        ),
        migrations.AlterModelOptions(
            name="detailconsultation",
            options={"verbose_name": "세부진료들"},
        ),
        migrations.AlterField(
            model_name="consultation",
            name="amount",
            field=models.IntegerField(verbose_name="금액"),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="consultation_date",
            field=models.DateTimeField(auto_now=True, verbose_name="진료날짜"),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="description",
            field=models.TextField(verbose_name="설명"),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="doctor_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="doctors.doctor",
                verbose_name="의사",
            ),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="patient_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="patients.patient",
                verbose_name="환자",
            ),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="reservation_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="reservations.reservation",
                verbose_name="예약번호",
            ),
        ),
        migrations.AlterField(
            model_name="detailconsultation",
            name="amount",
            field=models.IntegerField(verbose_name="금액"),
        ),
        migrations.AlterField(
            model_name="detailconsultation",
            name="consultation_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="consultations.consultation",
                verbose_name="진료번호",
            ),
        ),
        migrations.AlterField(
            model_name="detailconsultation",
            name="name",
            field=models.CharField(max_length=200, verbose_name="세부 진료명"),
        ),
    ]
