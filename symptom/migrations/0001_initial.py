# Generated by Django 3.0.4 on 2020-04-26 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consult', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('consult', models.ManyToManyField(to='consult.Consult')),
                ('parent_symptom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='symptom.Symptom')),
            ],
        ),
    ]
