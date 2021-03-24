# Generated by Django 3.1.7 on 2021-03-24 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'certifications',
            },
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('how_to_study', models.CharField(max_length=100)),
                ('study_time', models.CharField(max_length=30)),
                ('certification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certifications.certifications')),
            ],
            options={
                'db_table': 'experiences',
            },
        ),
    ]
