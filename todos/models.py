from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_at = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.title