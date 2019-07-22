from django.urls import path

from classroom import views

urlpatterns = [
  path('', views.index),
  path('courses', views.courses, name="courses"),
  path('courses/<int:id>', views.course, name="get_course"),
  path('courses/<int:course_id>/content/<int:id>', views.content, name="get_content"),
]
