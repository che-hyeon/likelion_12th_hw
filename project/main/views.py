from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.files.storage import default_storage

from .models import Post

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
    return render(request, 'main/post-in.html', {'post':post})

def create(request):
    new_post = Post()

    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
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

    return redirect('main:post_out', new_post.id)

def update(request, id):
    update_post = Post.objects.get(pk=id)

    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
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

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def delete(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    default_storage.delete(delete_post.image.path)
    return redirect('main:post')