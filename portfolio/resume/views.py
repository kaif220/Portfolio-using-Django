from django.shortcuts import render
from .models import Project, Experience, Skill

def home(request):
    skills = Skill.objects.all()
    return render(request, 'resume/home.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'resume/projects.html', {'projects': projects})

def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'resume/experience.html', {'experiences': experiences})
