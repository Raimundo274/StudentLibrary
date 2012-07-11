from django.db import models

# Create your models here.


class Student(models.Model):
	name = models.CharField(max_length=255)
	
	school = models.CharField(max_length=255)
	
	grade = models.CharField(max_length=255)
	
	def print_sentence(self, name, school, grade):
            return "The student %s goes to %s and is in %s"(self.name, self.school, self.grade)

	def __unicode__(self):
		return self.name
	


	
  
	
	
