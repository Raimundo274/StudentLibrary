from studentinfo.models import Student
from django.http import HttpResponse


def listofnames(request):
	
	return HttpResponse("Something goes in here that is the name of the student".Student.prints_a_sentence(), "test")

