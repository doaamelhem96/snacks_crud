# Generated by Django 4.2.3 on 2023-07-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_alter_snack_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='description',
            field=models.TextField(),
        ),
    ]