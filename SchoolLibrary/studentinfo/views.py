from studentinfo.models import Student
from django.template import Context, loader
from django.http import HttpResponse


	
def listofnames(request):
	#l = Student(name='List of Students', tagline='All the 		students in database.')
	#l.save()
	all_students = Student.objects.all()	
	#return HttpResponse(all_students)
	t = loader.get_template('studentinfo/allnames.html')
    	c = Context({
        	'all_students': all_students,
  	})
    	return HttpResponse(t.render(c))


def individual_student(request, studentinfo_id):
    for i in listofnames(Student):

        return HttpResponse("This is %s."% Student.print_sentence(Student.name))



