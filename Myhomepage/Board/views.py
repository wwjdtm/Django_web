from django.shortcuts import render

def postview(request,post_id):
    #your code
    Post.post_views=Post.post_views+1
    Post.post_views.save()
    #your code
