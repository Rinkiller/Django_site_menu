# Generated by Django 4.2.6 on 2023-11-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='Ingredients',
            field=models.TextField(default=str),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipes',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]