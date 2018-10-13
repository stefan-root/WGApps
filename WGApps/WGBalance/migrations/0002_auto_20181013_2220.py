# Generated by Django 2.1.1 on 2018-10-13 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WGBalance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WGBalance.Bill'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]