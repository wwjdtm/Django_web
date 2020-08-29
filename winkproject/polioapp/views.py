from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pblog, Nblog
from django.utils import timezone
from django import forms

# Create your views here.c
def home(request):
    return render(request,'home.html')

def Project(request):
    blogs = Pblog.objects.order_by('-id')
    return render(request, 'Project.html', {'blogs': blogs})

def News(request):
    newss = Nblog.objects.order_by('-id')
    return render(request, 'News.html', {'newss': newss})

def Pdetail(request, blog_id):
    blog_detail = get_object_or_404(Pblog, pk=blog_id)
    return render(request, 'Pdetail.html', {'blog': blog_detail})


def Ndetail(request, news_id):
    news_detail = get_object_or_404(Nblog, pk=news_id)
    return render(request, 'Ndetail.html', {'news': news_detail})


def Contact(request):
    return render(request,'Contact.html')
    
def Create(request):
    return render(request, 'Create.html')

def postcreate(request):
    if request.GET['boardname'] == "Projects":
        blog = Pblog()
        blog.p_boardname = "Project"
        blog.p_title = request.GET['title']
        blog.p_body = request.GET['body']
        blog.p_pub_date = timezone.datetime.now()
        blog.p_link = request.GET['link']
        
        blog.save()
        return redirect('/polioapp/Pdetail/' + str(blog.id))

    else:
        blog = Nblog()
        blog.n_boardname = "News"
        blog.n_title = request.GET['title']
        blog.n_body = request.GET['body']
        blog.n_pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/polioapp/Ndetail/' + str(blog.id))





def new(request):
    return render(request,'new.html')

def Pdelete(request, blog_id):
    blog = Pblog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/polioapp/Project/')

def Ndelete(request, news_id):
    news = Nblog.objects.get(id=news_id)
    news.delete()
    return redirect('/polioapp/News/')

def update(request, blog_id):
    blog = Pblog.objects.get(id=blog_id)

    if request.method == "POST":
        blog.p_title = request.POST['title']
        blog.p_body = request.POST['body']
        blog.p_pub_date = timezone.datetime.now()
        blog.p_link = request.POST['link']
        blog.save()
        return redirect('/polioapp/Pdetail/' + str(blog.id))

    else:
        return render(request, 'update.html')