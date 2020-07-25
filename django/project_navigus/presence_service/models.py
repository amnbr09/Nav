from django.db import models

class Doc(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date published')
    mod_date = models.DateTimeField('Modified date', auto_now_add= True)
    pdf = models.FileField(upload_to='Docs/')

class Viewers(models.Model):
    doc = models.ForeignKey(Doc, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    avatar = models.ImageField(height_field=None, width_field=None)
    isonline = BooleanField(default=False)
    last_visit = models.DateTimeField('Modified date', auto_now_add= True)
    