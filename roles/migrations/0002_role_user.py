# Generated by Django 5.0.6 on 2024-07-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_detailuser_role_remove_detailuser_status"),
        ("roles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="role",
            name="user",
            field=models.ManyToManyField(to="core.detailuser"),
        ),
    ]
