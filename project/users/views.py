from django.shortcuts import render
from main.models import Post

# Create your views here.

def mypage(request):
    username = request.user.username
    my_posts = Post.objects.filter(writer=username)
    return render(request, 'users/mypage.html', {'my_posts':my_posts})