# Generated by Django 4.2.7 on 2023-11-15 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='club',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='std_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
