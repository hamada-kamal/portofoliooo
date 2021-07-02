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
    
    
    # send email

    # if request.method == 'POST':
    #     email = request.POST['email']
    #     subject = request.POST['subject']
    #     message = request.POST['message']

    #     send_mail(
    #         subject,
    #         message,
    #         email,
    #         [settings.EMAIL_HOST_USER],

    #     )
    return render(request,'base/index.html', {'info': info, 'all_jobs':all_jobs, 'skills1':skills1, 'skills2':skills2, 'achievements': achievements})


# def contact(request):
#     if request.method == 'POST':
#         # name = request.POST['name']
        
#         message = EmailMessage()
#         message['subject']= request.POST['subject']
#         message['from']= request.POST['email']
#         message['to']='hamadakamal819@gmail.com'

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login("hamadakamal819@gmail.com","messanger8000")
#         server.send_message(message)
#         server.quit()
#     return render(request,'base/contact.html', {})