from django.db import models

class StudentProfile(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Full Name")

    university_id = models.CharField(max_length=20, unique=True, verbose_name="University ID Number")

    age = models.IntegerField(verbose_name="Age")

    date_of_birth = models.DateField(verbose_name="Date of Birth")

    address = models.TextField(verbose_name="Address")

    salary = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Salary")

    photo = models.ImageField(upload_to='student_photos/', verbose_name="Photo")

    def __str__(self):
        return self.full_name