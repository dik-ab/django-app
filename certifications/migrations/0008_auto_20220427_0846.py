# Generated by Django 3.1.7 on 2022-04-26 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifications', '0007_auto_20220421_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiences',
            name='faculty',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='experiences',
            name='motivation',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='experiences',
            name='recommend_class',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
    ]