from django.db import models

# Create your models here.
DEPARTMENT_CHOICES = (
    ('IT', 'Information Technology'),
    ('ECE', 'Electronics and Communication Engineering'),
    ('ICE', 'Instrumentation and Control Engineering'),
    ('EE', 'Electrical Engineering'),
    ('CE', 'Civil Engineering'),
    ('A', 'Architecture'),
)

YEAR_CHOICES = (
    ('First Year', 'First Year'),
    ('Second Year', 'Second Year'),
    ('Third Year', 'Third Year'),
    ('Final Year', 'Final Year'),
)


class Student(models.Model):
    profilePic = models.ImageField(upload_to='profilePic/', blank=True)
    name = models.CharField(max_length=100)
    studentID = models.CharField(max_length=8, primary_key=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    dob = models.DateField()
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES, default='IT')
    year = models.CharField(max_length=11, choices=YEAR_CHOICES, default='FE')

    def __str__(self):
        return self.studentID


class Search(models.Model):
    studentID = models.CharField(max_length=8, primary_key=True)
