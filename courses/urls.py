from django.urls import path, include
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.course_list, name='list'),
]
