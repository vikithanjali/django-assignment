from django.shortcuts import render, redirect
# Create your views here.
# pages/views.py
from django.views.generic import TemplateView
import smtplib
from .forms import Userform
from django.http import HttpResponse
from .filehander import handle_uploaded_file
from .resumeparser import get_resume_data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


from .models import Skill


class HomePageView(TemplateView):
    template_name = 'home.html'


def conformemail(request):
    if request.method == 'POST':
        username = request.POST['username']
        # we have to create smtp session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # Start TLS for security TLS means Transport Layer Security
        s.starttls()
        # Authentication
        sender = "madugulavikithanjali@gmail.com"
        passward = "Cseb522@8"
        s.login(sender, passward)
        message = "<h1>Authentication successfull</h1>"
        # sending mail
        s.sendmail(sender, username, message)
        # terminating session
        s.quit()
        return redirect("filehandler")


def filehandler(request):
    if request.method == 'POST':
        file = Userform(request.POST, request.FILES)
        if file.is_valid():
            file = request.FILES['file']
            handle_uploaded_file(file)
            resume_data = get_resume_data(file)
            skills = resume_data['skills']
            user_name = User.objects.get(username=request.POST['username'])
            for i in skills:
                skill = Skill(user_id=user_name, skill=i)
                skill.save()
            return HttpResponse("File uploaded successfuly")
    else:
        form = Userform()
        return render(request, "fileupload.html", {'form': form})


def get_skill_search(request):
    if request.method == "POST":
        skill = request.POST['skill']
        values = Skill.objects.filter(skill=skill)
        l =[]
        for value in values.all():
            data={}
            data['skill']=value.skill
            user_obj=User.objects.get(username=value.user_id)
            data['username']=user_obj.username
            l.append(data)
        return render(request, "user_data.html", {'user_data':l})
    else:
        return render(request, "skill_search.html", {})


def admin_login(request):
    if request.method == "POST":
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('get_skill_search')
    else:
        return redirect('home')
