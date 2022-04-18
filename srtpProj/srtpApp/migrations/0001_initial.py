# Generated by Django 3.2.5 on 2022-04-01 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=64, verbose_name='Course Name')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_num', models.IntegerField(verbose_name='Which week')),
                ('weekday_num', models.IntegerField(choices=[(1, '周一'), (2, '周二'), (3, '周三'), (4, '周四'), (5, '周五')], verbose_name='Which day in a week')),
                ('section_num', models.IntegerField(verbose_name='Which section')),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srtpApp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stuID', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='Student ID')),
                ('stuname', models.CharField(max_length=32, verbose_name="student's name")),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srtpApp.classgrade')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('focus_num', models.IntegerField(verbose_name='Focus Times')),
                ('signin_bool', models.BooleanField(verbose_name='Sign in？')),
                ('signin_time', models.DateTimeField(verbose_name='Sign in Time')),
                ('sectionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srtpApp.section')),
                ('stuID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srtpApp.student')),
            ],
        ),
    ]