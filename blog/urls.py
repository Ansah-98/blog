from django.urls import path
from blog.views import post_list,post_detail,PostListView,post_share

urlpatterns  = [
    path('',post_list, name = 'post_l'),
    path('<int:pk>',post_detail,name = 'post_detail'),
    path('post', PostListView.as_view(),name ='postclass'),
    path('share/<int:pk>',post_share, name = 'share_post')]