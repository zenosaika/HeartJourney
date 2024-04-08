from django.shortcuts import render
from Blog.models import Blog

def homepage(req):
    blogs = Blog.objects.all()
    return render(req, 'HeartJourney/homepage.html', {'blogs': blogs})
