from django.shortcuts import render
from django.http import Http404
from django.views.generic import View, ListView, DetailView

from classroom import models

# Create your views here.
class Index(View):
  def get(self, request):
    courses = models.Course.objects.filter(recommended = True)
    context = {
      "recommended_courses": courses
    }
    return render(request, 'classroom/index.html', context)

def index(request):
  courses = models.Course.objects.filter(recommended = True)

  context = {
    "recommended_courses": courses
  }
  return render(request, 'classroom/index.html', context)

class Courses(ListView):
  model = models.Course
  template_name = 'classroom/courses.html'
  context_object_name = 'courses'

def courses(request):
  # query = request.GET['query'] if 'query' in request.GET else ''
  query = request.GET.get('query', '')
  courses = models.Course.objects.filter(name__icontains = query)

  context = {
    "courses": courses
  }
  return render(request, 'classroom/courses.html', context)

class Course(DetailView):
  model = models.Course
  template_name = 'classroom/course.html'
  context_object_name = 'course'

def course(request, id):
  course = models.Course.objects.get(id = id)

  context = {
    "course": course
  }
  return render(request, 'classroom/course.html', context)

class Content(DetailView):
  context_object_name = 'content'

  def get_queryset(self):
    return models.Course.objects.get(id = self.kwargs['course_id']).contents

  def get_template_names(self):
    content = self.get_object()
    template_name = ''
    if content.content_type == 'pdf':
      template_name = 'classroom/content_pdf.html'
    elif content.content_type == 'youtube':
      template_name = 'classroom/content_yt.html'
    elif content.content_type == 'image':
      template_name = 'classroom/content_img.html' 
    return template_name

def content(request, course_id, id):
  # content = models.Content.get(id = id)
  course = models.Course.objects.get(id = course_id)
  content = course.contents.get(id = id)

  # if not content in course.contents.all():
  #   raise Http404()

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
