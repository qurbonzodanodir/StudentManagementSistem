# Generated by Django 4.2 on 2024-04-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(related_name='teacher', to='api.teacher'),
        ),
    ]
