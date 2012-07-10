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

