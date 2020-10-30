# Generated by Django 2.2.8 on 2020-10-27 19:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre del invitado')),
                ('universidad', models.TextField(validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='Universidad del invitado')),
                ('email', models.EmailField(blank=True, help_text='Escriba la dirección de correo hola@ins.edu.bo', max_length=250)),
                ('fotografia', models.ImageField(blank=True, help_text='Suba imagenes (jpg, gif, png)', upload_to='invitados/')),
                ('ocultar', models.BooleanField(default=False, verbose_name='Plataforma descontinuada')),
            ],
            options={
                'verbose_name_plural': 'Invitados',
                'ordering': ['id'],
            },
        ),
    ]
