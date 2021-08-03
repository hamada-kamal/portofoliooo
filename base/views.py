from email import message
from django.shortcuts import render
from .models import About, Job, Skill, Achievement
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from email.message import EmailMessage


def home(request):
    info =  About.objects.first()
    all_jobs = Job.objects.all()
    all_skills = Skill.objects.all()
    have = all_skills.count() / 2
    skills1 = all_skills[0:have]
    skills2 = all_skills[have:]
    achievements = Achievement.objects.all()
    return render(request,'base/index.html', {'info': info, 'all_jobs':all_jobs, 'skills1':skills1, 'skills2':skills2, 'achievements': achievements})

