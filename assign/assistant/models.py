from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('assistant:post_detail',kwargs={'pk':self.pk})

class Task(models.Model):
    
    class Meta:
        permissions = (
            ("create_post", "Can create announcement"),
            ("view_contact","Can view emergency contact"),
            ("create_review","Doctor create review"),
        )

class Contact(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

class Description(models.Model):
    functionality = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    published_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.functionality

class HealthStatus(models.Model):
    patientid = models.OneToOneField(User,primary_key=True)
    status = models.TextField()
    def __str__(self):
        return str(self.patientid)

class Comment(models.Model):
    post = models.ForeignKey('assistant.HealthStatus', related_name='recommendation')
    doctor = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text