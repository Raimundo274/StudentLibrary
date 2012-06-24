from django.db import models

# Create your models here.


class Student(models.Model):
	name = models.CharField(max_length=255)
	school = models.CharField(max_length=255)
	grade = models.CharField(max_length=255)
	def prints_a_sentence(self):
		return "The student %s is enrolled in %s and is in %s" %(self.name, self.school, self.grade)
	 
	
	
