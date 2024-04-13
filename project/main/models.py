from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    writer = models.CharField(max_length=20)
    write_date = models.DateTimeField()

    sender_place = models.TextField()
    sender_post_num = models.IntegerField()

    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    reciever_place = models.TextField()
    reciever_post_num = models.IntegerField()

    reciever = models.CharField(max_length=20)
    body = models.TextField()
    sender = models.CharField(max_length=20)

    def __str__(self):
        return self.title