# Generated by Django 5.0.6 on 2024-10-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Passworld', models.CharField(max_length=255)),
                ('Gmail', models.CharField(max_length=255)),
            ],
        ),
    ]
