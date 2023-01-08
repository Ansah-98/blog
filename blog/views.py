from django.views.generic import ListView
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.models import Post
# Create your views here.

def post_list(request):
    posts  = Post.objects.all()
    # paginator = Paginator(posts,3)
    # page = request.GET.get('page')
    # try:
    #     pages  = paginator.page(page)

    # except PageNotAnInteger:
    #     pages = paginator.page(1)
    # except EmptyPage:
    #     pages = paginator.page(paginator.num_pages)

    return render(request,'blog/list.html',{'posts':posts })
class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name ='blog/list.html'

def post_detail(request,id):
    post = Post.objects.get(id = id)

    return render(request,'blog/detailed.html',{'post':post})