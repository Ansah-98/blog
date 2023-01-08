from django.shortcuts import render

# Create your views here.
from blog.models import Post

def post_list(request):
    posts  = Post.objects.all()
    return render(request,'blog/list.html',{'posts':posts})

def post_detail(request,id):
    post = Post.objects.get(id = id)

    return render(request,'blog/detailed.html',{'post':post})