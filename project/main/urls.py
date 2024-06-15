from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "main"
urlpatterns = [
    path('', django_mtv, name='django_mtv'),
    path('free', free_page, name='free_page'),
    path('post', post, name='post'),
    path('new-post', new_post, name="new-post"),
    path('create', create, name="create"),
    path('<int:id>', post_out, name='post_out'),
    path('post_in/<int:id>', post_in, name="post_in"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('tag-list', tag_list, name="tag-list"),
    path('tag-posts/<int:tag_id>', tag_posts, name="tag_posts"),
    path('delete-comment/<int:comment_id>', delete_comment, name="delete_comment"),
    path('likes/<int:post_id>', likes, name="likes"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)