from django.db import models

# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=255, null=False, blank=False)
	email = models.EmailField(unique=True, null=False, blank=False)
	photo = models.ImageField(upload_to='img', null=True, blank=True)

	def __str__(self) -> str:
		return self.name

