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
        indid = Student.objects.get(id= studentinfo_id)
        indsentence = 'The student %s, goes to %s and is enrolled in %s' % (indid.name, indid.school, indid.grade)
        indt = loader.get_template('studentinfo/indstudent.html')
        indc = Context ({
            'indsentence': indsentence,
            })

        return HttpResponse(indsentence,"indt.render(indc)")
        #I still need to make a template to display the sentence,
        # the return above is just to test that it works.


