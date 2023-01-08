from django.urls import path
from blog.views import post_list,post_detail,PostListView

urlpatterns  = [
    path('',post_list, name = 'post_l'),
    path('<int:pk>',post_detail,name = 'post_d'),
    path('post', PostListView.as_view(),name ='postclass')]