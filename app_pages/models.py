from django.utils import  timezone

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User=get_user_model()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='teacher_images/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    course_name = models.CharField(max_length=100)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name


class Dars(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    video_url = RichTextField(blank=True)
    video = models.FileField(upload_to='dars_videos/', blank=True, null=True)

    description = models.TextField()
    text = RichTextField()
    file = models.FileField(upload_to='dars_files/')
    likes=models.ManyToManyField(User,related_name='post')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    additions=RichTextField(blank=True,null=True)
    view_count=models.IntegerField(default=0)

    def __str__(self):
        return self.name


class NewsTeacher(models.Model):
    picture = models.ImageField(upload_to='news_images/',blank=True,null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    text = RichTextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    dars = models.ForeignKey(Dars, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.user.username} on {self.dars.name}'


class Bitriuvchilar(models.Model):
    name=models.CharField(max_length=100)
    mudat=models.CharField(max_length=255)
    description=models.TextField()
    date = models.DateField()
    image=models.ImageField(upload_to="Biturivchilar/images")

    def __str__(self):
        return self.name
