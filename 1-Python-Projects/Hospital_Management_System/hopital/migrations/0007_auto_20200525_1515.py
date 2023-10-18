# Generated by Django 2.2.6 on 2020-05-25 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hopital', '0006_auto_20200525_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='last_attend',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='salary',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Fee_Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_date', models.DateField(null=True)),
                ('paid', models.IntegerField(null=True)),
                ('outstanding', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('pat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hopital.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20, null=True)),
                ('year', models.CharField(max_length=20, null=True)),
                ('attend', models.IntegerField(null=True)),
                ('doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hopital.Doctor')),
            ],
        ),
    ]