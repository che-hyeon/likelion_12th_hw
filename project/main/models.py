from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    write_date = models.DateTimeField()

    sender_place = models.TextField()
    sender_post_num = models.IntegerField()

    image = models.ImageField(upload_to="post/", blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    reciever_place = models.TextField()
    reciever_post_num = models.IntegerField()

    reciever = models.CharField(max_length=20)
    body = models.TextField()
    sender = models.CharField(max_length=20)
    
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    write_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title + " : " + self.content[:20] + " by " + self.writer.profile.nickname