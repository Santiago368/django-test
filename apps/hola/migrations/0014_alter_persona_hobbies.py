# Generated by Django 4.2.3 on 2023-07-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hola', '0013_persona_hobbies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='hobbies',
            field=models.ManyToManyField(blank=True, to='hola.hobbies'),
        ),
    ]
