from django.db import models

class Doc(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date published')
    mod_date = models.DateTimeField('Modified date', auto_now_add= True)
    pdf = models.FileField(upload_to='Docs/')

    def __str__(self):
        return self.title

from channels.generic.websocket import WebsocketConsumer
from channels_presence.models import Room

class MyConsumer(WebsocketConsumer):
    def connect(self):
        super().connect()
        Room.objects.add("some_room", self.channel_name, self.scope["user"])

    def disconnect(self, close_code):
        Room.objects.remove("some_room", self.channel_name)

    def receive(self, close_code):
        Presence.objects.touch(self.channel_name)

class Viewers(models.Model):
    doc = models.ForeignKey(Doc, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,height_field=None, width_field=None)
    isonline = models.BooleanField(default=False)
    last_visit = models.DateTimeField('Modified date', auto_now_add= True)
    
    def __str__(self):
        return self.name

    def current_viewers(self):
        online = {name:[],avatar:[]}
        if self.isonline == True:
            online[name] = self.name
            online[avatr] = self.avatar
        return online

    def past_viewers(self):
        return self.last_visit