from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Course, Lesson


# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    # response = ', '.join([str(course) for course in courses])
    # return HttpResponse(response)
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request,pk):
    # course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course,pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def lesson_detail(request, course_pk, lesson_pk):
    lesson = get_object_or_404(Lesson, course_id=course_pk, pk=lesson_pk)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})
