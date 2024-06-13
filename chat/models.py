from django.db import models
from django.conf import settings


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='message_images/', blank=True, null=True)  # Изображение сообщения

    def __str__(self):
        return f'{self.user.username} - {self.content}'
