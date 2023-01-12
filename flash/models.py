from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class FCard(models.Model):
    subject = models.CharField(max_length=20)
    question = models.TextField()
    answer = models.TextField()
    date_created = models.DateField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.subject
    
    
    def get_absolute_url(self):
        return reverse('flash-detail', kwargs={"pk": self.pk})
    
    
