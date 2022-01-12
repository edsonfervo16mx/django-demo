from django.contrib import admin

# Register your models here.
from .models import Course, Lesson


# Relation models in Admin
class LessonInline(admin.StackedInline):
    model = Lesson


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
