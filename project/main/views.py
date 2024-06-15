from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.files.storage import default_storage

from .models import Post, Comment, Tag

# Create your views here.

def django_mtv(request):
    return render(request, 'main/django_mtv.html')

def free_page(request):
    return render(request, 'main/free_page.html')

def post(request):
    posts = Post.objects.all()
    return render(request, 'main/post.html', {'posts': posts})

def new_post(request):
    return render(request, 'main/new-post.html')

def post_out(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'main/post-out.html', {'post':post})

def post_in(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/post-in.html', {'post':post, 'comments' : comments})
    elif request.method == 'POST':
        new_comment = Comment()
        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.write_date = timezone.now()

        new_comment.save()

        return redirect('main:post_in', id)

def create(request):
    if request.user.is_authenticated:
        new_post = Post()

        new_post.title = request.POST['title']
        new_post.writer = request.user
        new_post.write_date = timezone.now()

        new_post.sender_place = request.POST['sender_place']
        new_post.sender_post_num = request.POST['sender_post_num']
        new_post.image = request.FILES.get('image')
        new_post.reciever_place = request.POST['reciever_place']
        new_post.reciever_post_num = request.POST['reciever_post_num']

        new_post.reciever = request.POST['reciever']
        new_post.body = request.POST['body']
        new_post.sender = request.POST['sender']

        new_post.save()

        words = new_post.body.split(' ')
        tag_list = []

        for w in words:
            if len(w)>0:
                if w[0] == '#':
                    tag_list.append(w[1:])

        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag.id)
        
        return redirect('main:post_out', new_post.id)
    

    else:
        return redirect('accounts:login', new_post.id)

def update(request, id):
    update_post = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_post.writer:
        update_post.title = request.POST['title']
        update_post.write_date = timezone.now()

        update_post.sender_place = request.POST['sender_place']
        update_post.sender_post_num = request.POST['sender_post_num']
        if request.FILES.get('image'):
            update_post.image = request.FILES.get('image')
        update_post.reciever_place = request.POST['reciever_place']
        update_post.reciever_post_num = request.POST['reciever_post_num']

        update_post.reciever = request.POST['reciever']
        update_post.body = request.POST['body']
        update_post.sender = request.POST['sender']

        update_post.save()

        return redirect('main:post_out', update_post.id)
    

    return redirect('accounts:login', update_post.id)

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def delete(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    if delete_post.image and delete_post.image.path:
        default_storage.delete(delete_post.image.path)
    else:
        pass
    return redirect('main:post')

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag-list.html', { 'tags' : tags })

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag-posts.html', {
        'tag' : tag,
        'posts' : posts
    })

def delete_comment(request, comment_id):
    
    delete_comment = Comment.objects.get(pk=comment_id)
    post = get_object_or_404(Post, pk=delete_comment.post.id)
    delete_comment.delete()

    return render(request, 'main/post-in.html',{ 'post' : post })

def likes(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('main:post_out', post.id)
