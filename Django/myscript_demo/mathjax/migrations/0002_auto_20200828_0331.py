# Generated by Django 3.0.8 on 2020-08-27 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathjax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=500),
        ),
    ]
