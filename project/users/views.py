from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from main.models import Post
# Create your views here.

def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    username = request.user
    my_posts = Post.objects.filter(writer = username)
    context = {
        'user':user,
        'followings': user.profile.followings.all(),
        'followers': user.profile.followers.all(),
        'my_posts' : my_posts
    }
    return render(request, 'users/mypage.html', context)

def follow(request, id):
    user = request.user 
    followed_user = get_object_or_404(User, pk=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)
