# Generated by Django 5.0.1 on 2024-01-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoList",
            fields=[
                ("title", models.CharField(max_length=256)),
                ("description", models.TextField()),
                ("startDate", models.DateTimeField()),
                ("itemID", models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
