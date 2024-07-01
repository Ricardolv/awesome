
from django.contrib import admin
from django.urls import path
from a_posts.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('post/crete/', post_create_view, name='post-create'),
    path('post/delete/<pk>/', post_delete_view, name='post-delete'),
    path('post/edit/<pk>/', post_edit_view, name='post-edit'),
    path('post/page/<pk>/', post_page_view, name='post'),
]
