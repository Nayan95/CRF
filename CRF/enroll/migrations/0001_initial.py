# Generated by Django 3.1.6 on 2021-03-21 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('q_id', models.IntegerField(primary_key=True, serialize=False)),
                ('q_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_text', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.patient')),
                ('q_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.question')),
            ],
        ),
    ]
