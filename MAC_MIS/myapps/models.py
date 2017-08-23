from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class MyUser(User):
    is_Faculty = models.BooleanField(default=False)
    is_Student = models.BooleanField(default=False)
    phone = models.IntegerField(blank=True, null=True)

class Staff(MyUser):
    Staff_start = models.DateTimeField(blank=True, null=True)
    Staff_end = models.DateTimeField(blank=True, null=True)
    PROVINCE_CHOICES = (
        ('AB', 'Alberta'),  # First value is stored in db, the second is descriptive
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec'),
        ('BC', 'British Columbia'),
        ('NS', 'Nova Scotia'),
        ('SK', 'Saskatchewan'),
        ('NB', 'New Brunswick'),
        ('NL', 'Newfoundland and Labrador'),
        ('PE', 'Prince Edward Island'),
        ('NT', 'Northwest Territories'),
        ('YT', 'Yukon'),
        ('NU', 'Nunabut')
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    class Meta:
        verbose_name = "staff"

class Faculty(MyUser):
    Fac_start = models.DateTimeField(blank=True, null=True)
    Fac_end = models.DateTimeField(blank=True, null=True)
    PROVINCE_CHOICES = (
        ('AB', 'Alberta'),  # First value is stored in db, the second is descriptive
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec'),
        ('BC', 'British Columbia'),
        ('NS', 'Nova Scotia'),
        ('SK', 'Saskatchewan'),
        ('NB', 'New Brunswick'),
        ('NL', 'Newfoundland and Labrador'),
        ('PE', 'Prince Edward Island'),
        ('NT', 'Northwest Territories'),
        ('YT', 'Yukon'),
        ('NU', 'Nunabut')
    )
    POSITION_CHOICES = (
        ('Director', 'Director'),
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Instructor', 'Instructor'),
    )
    Fac_position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='Instructor')
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=50, choices=PROVINCE_CHOICES, default='ON')

    class Meta:
        verbose_name = "faculty"
        verbose_name_plural = "faculties"
    #     Faculty.user_permissions.add("fac_add", "fac_delete", "fac_modify", "fac_search")

class Student(MyUser):
    Stu_start = models.DateTimeField(blank=True, null=True)
    Stu_end = models.DateTimeField(blank=True, null=True)
    PROVINCE_CHOICES = (
        ('AB', 'Alberta'),  # First value is stored in db, the second is descriptive
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec'),
        ('BC', 'British Columbia'),
        ('NS', 'Nova Scotia'),
        ('SK', 'Saskatchewan'),
        ('NB', 'New Brunswick'),
        ('NL', 'Newfoundland and Labrador'),
        ('PE', 'Prince Edward Island'),
        ('NT', 'Northwest Territories'),
        ('YT', 'Yukon'),
        ('NU', 'Nunabut')
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    age = models.IntegerField(null=True, blank=True)
    GENDER_CHOICES = (
        ('F','Female'),
        ('M','Male'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='F')
    STATUS_CHOICES = (
        ('I', 'International'),
        ('C', 'Citizen')
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')
    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"

class Project(models.Model):
    Pro_ID = models.IntegerField(primary_key=True)
    Pro_title=models.CharField(max_length=200, default='Project title', verbose_name='title')
    Pro_start = models.DateTimeField()
    Pro_end = models.DateTimeField()
    Pro_description = models.CharField(max_length=200)
    Fac_ID = models.ForeignKey(Faculty)
    Stu_ID = models.ManyToManyField(Student)
    class Meta:
        permissions = (
            ("pro_add", "Add a new project"),
            ("pro_delete", "Delete this project"),
            ("pro_modify", "Modify this project"),
            ("pro_search", "Search projects"),
        )

    def __str__(self):
        return self.Pro_title

class Job(models.Model):
    Job_ID = models.IntegerField(primary_key=True)
    Job_company = models.CharField(max_length=100)
    Job_position = models.CharField(max_length=100)
    Job_address = models.CharField(max_length=100)
    Stu_ID = models.ManyToManyField(Student, verbose_name='Student name')
    class Meta:
        permissions = (
            ("job_add", "Apply a new job"),
            ("job_delete", "Delete this position"),
            ("job_modify", "Modify this job"),
            ("job_search", "Search job"),
        )

    def __str__(self):
        str = self.Job_position +", " + self.Job_company
        return str

    def all_stu(self):
        return ','.join([x.username for x in self.Stu_ID.all()])
