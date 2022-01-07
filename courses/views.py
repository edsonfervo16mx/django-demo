from django.shortcuts import render
from django.http import HttpResponse

from .models import Course


# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    response = ', '.join([str(course) for course in courses])
    return HttpResponse(response)
