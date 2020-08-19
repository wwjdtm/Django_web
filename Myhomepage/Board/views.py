from django.shortcuts import render, redirect
from .models import *
from .forms import BoardForm
from .forms import PostForm

def postview(request,post_id):
    #your code
    Post.post_views=Post.post_views+1
    Post.post_views.save()
    #your code

def create(request): #게시글작성하고db에저장되는부분
    if request.method=='POST':
        form =BoardForm(request.POST)
        if form.is_valid():
            form.save() #db에 저장하는부분
        # return redirect('/Myinfo/list')
    else: ##데이터입력폼
        form = BoardForm()

    return render(request, 'Myinfo/readPerson.html', {'form': form}) 

def Board(request):
    return render(request,'Myinfo/Board.html') #게시판화면보이기

# def makepost(request):
#     return render(request,'Myinfo/main.html') 