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





    path('new/', views.new, name='new'),
]