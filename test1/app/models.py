from django.db import models

# Create your models here.
CHOICES = (
    ("Male", "male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

CHOICE_YEAR = (
    ("1st Year", "1st Year"),
    ("2nd Year", "2nd Year"),
    ("3rd Year", "3rd Year"),
    ("4th Year", "4th Year"),
)

TYPE_FEES = (
    ("Fine", "Fine"),
    ("Fees", "Fees"),
    ("Other", "Other"),
)
# Student database


class StudentDatabase(models.Model):
    student_name = models.CharField(max_length=100, verbose_name='Student Name')
    fathers_name = models.CharField(max_length=100, verbose_name="Father's Name")
    dob = models.DateField(verbose_name='Date of Birth')
    gender = models.CharField(max_length=30, choices=CHOICES, verbose_name='Gender')
    course = models.CharField(max_length=30, verbose_name='Course')
    branch = models.CharField(max_length=30, verbose_name='Branch')
    contact1 = models.IntegerField(unique=True, verbose_name="Parent's contact")
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    doj = models.DateField(verbose_name='Date of Admission')
    year = models.CharField(max_length=30, choices=CHOICE_YEAR, verbose_name='Year')
    actual_fees = models.FloatField(max_length=20, verbose_name='Actual Amount')
    concession = models.FloatField(max_length=30, verbose_name='Concession')
    balance = models.FloatField(max_length=20, verbose_name='Balance')
    currently_paid = models.FloatField(max_length=20, verbose_name='Currently Paid')
    net_pay = models.FloatField(max_length=20, verbose_name='Net Payable')

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = 'Student database'
        verbose_name = 'Student Database'


# Fees payment database


class FeeDept(models.Model):
    student_name1 = models.CharField(max_length=50, verbose_name="Student Name")
    fathers_name = models.CharField(max_length=60, verbose_name="Father's Name")
    email=models.EmailField(verbose_name="Email")
    year = models.CharField(max_length=30, choices=CHOICE_YEAR, verbose_name='Year')
    fee_type = models.CharField(max_length=30, choices=TYPE_FEES, verbose_name='Type')
    fees_amount = models.FloatField(max_length=10, verbose_name='Amount')
    balance = models.FloatField(max_length=10, verbose_name='Balance')
    dos = models.DateTimeField(auto_now=True, verbose_name='Date')

    class Meta:
        db_table = 'Fees Detail'
        verbose_name = 'Fees Detail'


