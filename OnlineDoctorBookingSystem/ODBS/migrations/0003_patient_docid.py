# Generated by Django 3.2.20 on 2024-02-23 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ODBS', '0002_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='docid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ODBS.doctor'),
        ),
    ]
