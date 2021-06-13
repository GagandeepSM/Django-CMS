from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Content(models.Model):
	
	title = models.CharField(max_length=30)
	body = models.TextField(max_length=300)
	summary = models.TextField(max_length=60)
	# document_in_pdf = models.
	# categories = models.
	author = models.ForeignKey(User, on_delete=models.CASCADE) # if user gets deleted then his post will too but not vice versa


	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('content-detail', kwargs={'pk': self.pk})
