from taggit.models import Tag
from .forms import EmailForm,CommentForm
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.models import Post,Comment
from django.core.mail import send_mail
from django.db.models import Count
# Create your views here.

def post_list(request,tag_slug = None):

    posts  = Post.objects.all()
    tag = None 
    if tag_slug:
        tag = get_object_or_404( Tag, slug = tag_slug)

    # paginator = Paginator(posts,3)
    # page = request.GET.get('page')
    # try:
    #     pages  = paginator.page(page)

    # except PageNotAnInteger:
    #     pages = paginator.page(1)
    # except EmptyPage:
    #     pages = paginator.page(paginator.num_pages)

    return render(request,'blog/list.html',{'posts':posts ,'tag':tag})
def post_share(request,pk):
    post = Post.objects.get(pk= pk)
    sent_to= False
    if post is not None:
        if request.method =='POST':
            form = EmailForm(request.POST)
            if form.is_valid():
                post_url  = request.build_absolute_uri(post.get_absolute_url())
                cd = form.cleaned_data
                subject = f"{cd['name']} recommends you to read {post.title}"
                message =  f"Read {post.title} at {post_url} \n\n {cd['name']}'s comments:{cd['comments']}"
                send_mail(subject,message,'admin@myblog.com', cd['to'])
                sent_to = True
        else:
            form = EmailForm()
    return render(request,'blog/share.html',{'post':post
                                            ,'form':form,
                                            'sent': sent_to} )

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name ='blog/list.html'

def post_detail(request,pk):
    post = Post.objects.get(pk = pk)
    comments = post.comments.filter(active = True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post 
            new_comment.save()
    else:
        comment_form = CommentForm()
    post_tags_id = post.tags.values_list('id', flat = True)
    # similar_post  = Post.filter(tags_in =post_tags_id).exclude(id =post.id)
    # similar_post = similar_post.annotate(same_tags = Count('tags').order_by('-same_tags','-publish'))[:4]

    return render(request,'blog/detailed.html',
                            {'post':post,
                            'comments':comments,
                            'new_comment':new_comment,
                            'comment_form':comment_form,
                            })