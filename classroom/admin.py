from django.contrib import admin

from classroom import models

# Register your models here.
admin.site.register([
  models.Course,
  models.Content,
  models.Instructor
])
