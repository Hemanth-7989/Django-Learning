from django.shortcuts import render
from django.http import HttpResponse
from .models import Students


# Create your views here.
def students(request):
    students_list = list(Students.objects.all())
    return HttpResponse(students_list)
