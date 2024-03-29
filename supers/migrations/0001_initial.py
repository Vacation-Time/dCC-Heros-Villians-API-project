# Generated by Django 4.0.2 on 2022-02-17 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('super_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Super',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alter_ego', models.CharField(max_length=255)),
                ('primary_ability', models.CharField(max_length=255)),
                ('secondary_ability', models.CharField(max_length=255)),
                ('catchphrase', models.CharField(max_length=255)),
                ('super_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='super_type.supertype')),
            ],
        ),
    ]
