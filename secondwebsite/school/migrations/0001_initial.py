# Generated by Django 2.0.1 on 2018-01-19 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('class_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_amount', models.IntegerField(default=0)),
                ('frequency', models.IntegerField(default=0)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Classes')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('max_marks', models.IntegerField(default=0)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Classes')),
            ],
        ),
    ]
