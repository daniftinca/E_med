# Generated by Django 3.0.4 on 2020-04-26 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consult', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='consult',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consult.Consult'),
        ),
    ]
