# Generated by Django 4.1.5 on 2023-02-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_todo_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday_year',
            field=models.PositiveIntegerField(default=1990),
        ),
    ]