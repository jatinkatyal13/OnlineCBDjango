from django.shortcuts import render
from django.http import Http404

from classroom import models

# Create your views here.
def index(request):
  courses = models.Course.objects.filter(recommended = True)

  context = {
    "recommended_courses": courses
  }
  return render(request, 'classroom/index.html', context)

def courses(request):
  courses = models.Course.objects.all()

  context = {
    "courses": courses
  }
  return render(request, 'classroom/courses.html', context)

def course(request, id):
  course = models.Course.objects.get(id = id)

  context = {
    "course": course
  }
  return render(request, 'classroom/course.html', context)

def content(request, course_id, id):
  course = models.Course.objects.get(id = course_id)
  content = course.contents.get(id = id)

  context = {
    "content": content
  }
  template_name = ''
  if content.content_type == 'pdf':
    template_name = 'content_pdf.html'
  elif content.content_type == 'youtube':
    template_name = 'content_yt.html'
  elif content.content_type == 'image':
    template_name = 'content_img.html'

  return render(request, 'classroom/{}'.format(template_name), context)
