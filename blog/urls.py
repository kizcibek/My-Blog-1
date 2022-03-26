from django.urls import path

from blog.views import posts_list, PostDetail, tags_list, TagCreate, TagDetail


urlpatterns = [
    path('', posts_list, name='post_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url')

]