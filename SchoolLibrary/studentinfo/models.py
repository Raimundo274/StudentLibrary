from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    GRADE_OPTIONS = (
        (u'9th', u'Freshmen'),
        (u'10th', u'Sophomore'),
        (u'11th', u'Junior'),
        (u'12th', u'Senior'),
        (u'N/A' , u'Not Enrolled'),
    )
    grade = models.CharField(max_length =5, choices=GRADE_OPTIONS)
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/studentinfo/%i/" % self.id



class Teacher(models.Model):
    teacher_name = models.CharField(max_length =100)
    t_email = models.CharField(max_length = 100)
    t_subject = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.smallschoolname


class Libraries(models.Model):

    student_library = models.ForeignKey(Student)
    teacher_library = models.ForeignKey(Teacher)
    def __unicode__(self):
        return self.name
    #def get_absolute_url(self):
        #return "/%i/" % self.








