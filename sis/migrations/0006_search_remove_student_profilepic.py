# Generated by Django 4.0.6 on 2022-09-19 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0005_alter_student_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('studentID', models.CharField(max_length=8, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='profilePic',
        ),
    ]
