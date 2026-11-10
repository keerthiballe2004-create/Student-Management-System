from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    course = models.CharField(max_length=50)
    gender = models.CharField(
    max_length=10,
    choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    )

    address = models.TextField()

    profile_image = models.ImageField(
        upload_to='student_images/',
        blank=True,
        null=True
    )

    certificate = models.FileField(
        upload_to='certificates/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name