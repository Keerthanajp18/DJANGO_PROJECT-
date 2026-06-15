from django.db import models

# Create your models here.
class Student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    stud_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    class Meta:
        managed = False     #important
        db_table = 'students'    #match your actual table name
