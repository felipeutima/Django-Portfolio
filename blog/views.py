from urllib import request
from django.shortcuts import render
from .models import post
def render_posts(request):
    posts= post.objects.all()
    return render(request, 'posts.html',{'posts':posts})
# Create your views here.

def post_detail(request,post_id):
    return render(request,'post_detail.html',{"post":post_id})
