# Generated by Django 3.0.4 on 2020-04-26 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('thirdpartylogin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('date_of_birth', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('health_care_number', models.IntegerField()),
            ],
        ),
    ]