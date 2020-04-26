# Generated by Django 3.0.4 on 2020-04-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('problem_description', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('InWork', 'InWork'), ('Done', 'Done')], default='Pending', max_length=250)),
            ],
        ),
    ]
