# Generated by Django 4.0.6 on 2022-09-19 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0004_student_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Final Year', 'Final Year')], default='FE', max_length=11),
        ),
    ]
