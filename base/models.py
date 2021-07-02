from django.db import models
from django.db.models.base import Model
from django.db.models.fields import SlugField
from django.utils.text import slugify

class Job(models.Model):
    job_name = models.CharField(max_length=50)

    def __str__(self):
            return self.job_name


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
            return self.skill_name

class Achievement(models.Model):
    project_name = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to='myprojects_img/', blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)

    def __str__(self):
            return self.project_name



JOB_status = (
    ('Available','Available'),
    ('Unavailable','Unavailable'),
)
class About(models.Model):
    name = models.CharField(max_length=50)
    brief = models.TextField(max_length=100)
    avatar = models.ImageField(upload_to='profile_img/', blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_img/', blank=True, null=True)
    phone = models.TextField(max_length=11)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    freelance = models.CharField(max_length=15,choices=JOB_status)

    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linked_in_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    slug = models.SlugField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(About, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name


