from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('Project/', views.Project, name='Project'),
    path('News/', views.News, name='News'),
    path('Contact/', views.Contact, name='Contact'),
    path('Pdetail/<int:blog_id>/', views.Pdetail, name='Pdetail'),
    path('Ndetail/<int:news_id>/', views.Ndetail, name='Ndetail'),
    path('Create/', views.Create, name='Create'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('Pdelete/<int:blog_id>/', views.Pdelete, name='Pdelete'),
    path('Ndelete/<int:news_id>/', views.Ndelete, name='Ndelete'),
    path('Pupdate/<int:blog_id>/', views.Pupdate, name='Pupdate'),
    path('Nupdate/<int:news_id>/', views.Nupdate, name='Nupdate'),





    path('new/', views.new, name='new'),
]