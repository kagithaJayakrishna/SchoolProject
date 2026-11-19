from django.db import models

# Create your models here.
class Admission(models.Model):
    stu_name = models.CharField(max_length=10)
    stu_fname = models.CharField(max_length=10) 
    stu_age = models.IntegerField()
    stu_class = models.CharField(max_length=20)
    stu_fphone = models.CharField(max_length=10,unique=True)
    stu_fee = models.PositiveIntegerField()

    def __str__(self):
        return self.stu_name

    class Meta():
        verbose_name = "Admission"
        verbose_name_plural = "Admissions"