from django.urls import path
from .views import *

urlpatterns = [
    path('man/', all_posts, name="man"),
    path('post/<str:id>/', post_by_id, name="post-by-id"),
    path('create/post/', create_post, name="create-post"),
    path('update/post/<str:id>/', update_post, name="update-post"),
    path('delete/post/<str:id>/', delete_post, name='delete-post')
]
