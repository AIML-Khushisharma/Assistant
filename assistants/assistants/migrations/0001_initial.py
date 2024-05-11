# Generated by Django 5.0.4 on 2024-05-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
    ]
