from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from Myinfo.models import Myinfo
from .models import *
from .forms import MyinfoForm

def main(request):
    return render(request,'Myinfo/main.html')


def regPerson(request):
    return render(request, 'Myinfo/registerPerson.html')
################
# def regConPerson(request):
#     name = request.POST['name']
#     photo = request.POST['photo']
#     email = request.POST['email']
#     github_link = request.POST['github_link']
#     skill = request.POST['skill']
#     sns = request.POST['sns']
#     introduction = request.POST['introduction']
#
#     qp=Myinfo(name=name, photo=photo, email=email, github_link=github_link, skill=skill, sns=sns, introduction=introduction)
#     qp.save() #데이터베이스에저장
#
#     return HttpResponseRedirect(reverse('Myinfo:mainP')) #로그인하면메인화면으로정보넘겨줌
#############
def create(request):
    if request.method=='POST':
        form = MyinfoForm(request.POST)
        if form.is_valid():
            form.save() #db에 저장하는부분
            return redirect('/')
    else:
        form = MyinfoForm()

    return render(request, 'Myinfo/readPerson.html', {'form': form})




##############

# def mainPerson(request):
#     qp = Myinfo.objects.all()
#     context = {'Myinfo_list': qp}
#     return render(request, 'Myinfo/readPerson.html', context)
