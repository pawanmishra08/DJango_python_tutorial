from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank= True)
    receipe_name = models.CharField(max_length= 100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")
    receipe_view_count = models.IntegerField(default=1)

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department #Return department name in admin panel

    class Meta:
        ordering = ['department'] #Order departments alphabetically

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id #Return student ID in admin panel


class Subject(models.Model):
    subject_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.subject_name #Return subject name in admin panel

class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID,related_name="student", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name #Return student name in admin panel

    class Meta:
        ordering =  ['student_name'] #Order students alphabetically
        verbose_name = 'student'

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name= "studentmarks", on_delete= models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    marks =   models.IntegerField()

    def __str__(self):
        return f'{self.student.student_name } { self.subject.subject_name} '

    class Meta:
        unique_together = [ 'student', 'subject' ] #Ensure unique student-subject combination

class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name= "studentreportcard", on_delete= models.CASCADE)
    student_rank = models.IntegerField()
    date_of_report_card_generation = models.DateField(auto_now_add =True)

    class Meta:
        unique_together = ['student_rank', 'date_of_report_card_generation'] #Ensure unique rank-date combination

