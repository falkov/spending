# Generated by Django 2.0.6 on 2018-08-06 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_email_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordForEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_for_email', models.CharField(max_length=30)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.EmailAddress')),
            ],
        ),
    ]
