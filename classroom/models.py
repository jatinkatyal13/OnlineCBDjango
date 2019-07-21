from django.db import models

# Create your models here.
class Course(models.Model):
  name = models.CharField(max_length = 256)
  price = models.FloatField()
  description = models.TextField()
  instructor = models.ForeignKey('Instructor', on_delete = models.CASCADE)
  contents = models.ManyToManyField('Content')

  def __str__(self):
    return self.name

class Content(models.Model):
  CONTENT_CHOICES = [
    ('pdf', 'PDF'),
    ('youtube', 'YouTube Video'),
    ('image', 'Image')
  ]
  name = models.CharField(max_length = 256)
  content_type = models.CharField(max_length = 256, choices = CONTENT_CHOICES)

  def __str__(self):
    return self.name

class Instructor(models.Model):
  photo = models.URLField(null = True, blank = True)
  name = models.CharField(max_length = 256)
  email = models.EmailField()

  def __str__(self):
    return self.name
