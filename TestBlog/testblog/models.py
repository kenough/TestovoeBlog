from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    postname = models.CharField(max_length=100)
    date_post = models.DateTimeField(auto_now_add=True)
    post = models.TextField()
    permission = models.BooleanField(default=True)
    user_id = models.ForeignKey(User)
    
class Comments(models.Model):
    comment = models.TextField()
    date_com = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User)
    post_id = models.ForeignKey('Posts')

