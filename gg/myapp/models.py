from django.db import models

# Create your models here.
class student(models.Model):
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	age=models.CharField(max_length=100)
	def __str__(self):
		return self.first_name
